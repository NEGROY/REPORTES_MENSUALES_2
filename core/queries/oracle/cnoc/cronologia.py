from core.queries.oracle.base import BaseOracleQuery


class CronologiaQuery(BaseOracleQuery):
    SQL = """
        SELECT
            UPDATE_ACTION AS ULTIMO_COMENTARIO,
            "NUMBER",
            OPEN_TIME,
            CLOSE_TIME
        FROM probsummarym1
        WHERE "NUMBER" = :TICKET
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {
            'TICKET': self._normalize_ticket(self.params.get('ticket', ''))
        }

    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()

        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket
