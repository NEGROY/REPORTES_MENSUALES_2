from django.core.management.base import BaseCommand

from core.db.oracle.healthcheck import test_oracle_connection
from core.db.oracle.connection import oracle_config_status

# /* ******************************** */
class Command(BaseCommand):
    help = "Prueba la conexión a Oracle"

    def handle(self, *args, **options):
        self.stdout.write("=== Estado de configuración Oracle ===")
        config = oracle_config_status()

        for key, value in config.items():
            self.stdout.write(f"{key}: {value}")

        self.stdout.write("")
        self.stdout.write("=== Prueba de conexión Oracle ===")

        result = test_oracle_connection(close_after=True)

        if result.get("ok"):
            self.stdout.write(self.style.SUCCESS(result.get("message", "Conexión OK")))
            data = result.get("data", {})
            for key, value in data.items():
                self.stdout.write(f"{key}: {value}")
        else:
            self.stdout.write(self.style.ERROR(result.get("message", "Error de conexión")))
            if result.get("error"):
                self.stdout.write(self.style.ERROR(result["error"]))
