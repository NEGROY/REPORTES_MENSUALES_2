from core.queries.oracle.base import BaseOracleQuery


# DEFINIMOS LA CLASE DE CRONOLOGIA, para reutilziar la baseOracleQuery
# CronologiaQuery(params={'ticket': '12345'})
class CronologiaQuery(BaseOracleQuery):
    # CADENA ESTATICA DE SQL 
    SQL = """
        SELECT
            UPDATE_ACTION AS ULTIMO_COMENTARIO,
            "NUMBER",
            OPEN_TIME,
            CLOSE_TIME
        FROM probsummarym1
        WHERE "NUMBER" = :TICKET
    """
    # METODO REQUERIDO, ejecuta la query 
    def get_sql(self) -> str:
        return self.SQL

    # dicciionario, con los parametros de SQL 
    def get_params(self) -> dict:
        return {
            'TICKET': self._normalize_ticket(self.params.get('ticket', ''))
        }
    # apoya para el SRP, encapsula la logica de limpieza. 
    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()
        # si no empieza por F SE LA COLOCA 
        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket
    
    
# ------------------------------
# Endpoint 10: # http://127.0.0.1:8080/cronologia?falla_id=F6433510
# http://172.20.97.102:8080/cronologia/F6840709
# ------------------------------
