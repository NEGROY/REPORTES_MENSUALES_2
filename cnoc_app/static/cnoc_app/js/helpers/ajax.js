/* GET POST PUT DELETE */
/* GET POST PUT PATCH DELETE */

function getCookie(name) {
    const cookies = document.cookie ? document.cookie.split(';') : [];

    for (const rawCookie of cookies) {
        const cookie = rawCookie.trim();
        if (cookie.startsWith(`${name}=`)) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }

    return '';
}

function getCsrfToken() {
    return getCookie('csrftoken');
}

function buildUrl(url, params = null) {
    if (!params) {
        return url;
    }

    const searchParams = new URLSearchParams();

    Object.entries(params).forEach(([key, value]) => {
        if (value !== null && value !== undefined && value !== '') {
            searchParams.append(key, value);
        }
    });

    const queryString = searchParams.toString();
    return queryString ? `${url}?${queryString}` : url;
}

async function parseResponse(response) {
    const contentType = response.headers.get('content-type') || '';
    let data = null;

    if (contentType.includes('application/json')) {
        data = await response.json();
    } else {
        data = await response.text();
    }

    if (!response.ok) {
        const error = new Error(`HTTP ${response.status}`);
        error.status = response.status;
        error.data = data;
        throw error;
    }

    return data;
}

async function request(url, method = 'GET', data = null, params = null, headers = {}) {
    const finalUrl = buildUrl(url, params);

    const options = {
        method: method.toUpperCase(),
        credentials: 'same-origin',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            ...headers,
        },
    };

    if (['POST', 'PUT', 'PATCH', 'DELETE'].includes(options.method)) {
        options.headers['X-CSRFToken'] = getCsrfToken();
    }

    if (data !== null) {
        const isFormData = data instanceof FormData;

        if (isFormData) {
            options.body = data;
        } else {
            options.headers['Content-Type'] = 'application/json';
            options.body = JSON.stringify(data);
        }
    }

    const response = await fetch(finalUrl, options);
    return parseResponse(response);
}

export const ajax = {
    get(url, params = null, headers = {}) {
        return request(url, 'GET', null, params, headers);
    },

    post(url, data = {}, headers = {}) {
        return request(url, 'POST', data, null, headers);
    },

    put(url, data = {}, headers = {}) {
        return request(url, 'PUT', data, null, headers);
    },

    patch(url, data = {}, headers = {}) {
        return request(url, 'PATCH', data, null, headers);
    },

    delete(url, data = null, headers = {}) {
        return request(url, 'DELETE', data, null, headers);
    },
};

export { request };