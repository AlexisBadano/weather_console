from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

consola = Console()


def obtener_simbolo(codigo: int) -> str:
    """Devuelve un símbolo según el código meteorológico."""

    if codigo == 0:
        return "☀"
    elif codigo in (1, 2):
        return "⛅"
    elif codigo == 3:
        return "☁"
    elif codigo in (45, 48):
        return "🌫"
    elif codigo in (51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82):
        return "🌧"
    elif codigo in (71, 73, 75, 77, 85, 86):
        return "❄"
    elif codigo in (95, 96, 97, 99):
        return "⛈"

    return "?"


def mostrar_pronostico(dia: dict, titulo: str) -> Panel:
    """Construye un panel con el pronóstico del día."""

    fecha = datetime.strptime(dia["fecha"], "%Y-%m-%d")
    nombre_dia = fecha.strftime("%d/%m")

    simbolo = obtener_simbolo(dia["codigo_clima"])

    contenido = Group(
        Align.center(Text(nombre_dia, style="dim")),
        Align.center(Text(simbolo, style="bold bright_white")),
        Align.center(Text(dia["descripcion_clima"], style="bold bright_blue")),
        Align.center(Text(f'Máx. {dia["temperatura_maxima"]} °C',style="bold bright_white")
        ),
        Align.center(
            Text(
                f'Mín. {dia["temperatura_minima"]} °C',
                style="bold cyan"
            )
        ),
        Align.center(
            Text(
                f'Prob. lluvia: {dia["probabilidad_lluvia"]} %',
                style="dim"
            )
        )
    )

    return Panel(
        contenido,
        title=f"[bold bright_blue]{titulo}[/bold bright_blue]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 2)
    )


def mostrar_clima(clima: dict, ubicacion: dict) -> None:
    """Muestra el clima actual y el pronóstico de los próximos días."""

    clima_actual = clima["actual"]

    ciudad = Text(
        f'{ubicacion["nombre"]}, {ubicacion["pais"]}',
        style="white"
    )

    temperatura = Text(
        f'{clima_actual["temperatura"]} °C',
        style="bold bright_white"
    )

    descripcion = Text(
        clima_actual["descripcion_clima"],
        style="bold bright_blue"
    )

    indicadores = Table.grid(
        expand=True,
        padding=(1, 2)
    )

    indicadores.add_column(justify="center")
    indicadores.add_column(justify="center")
    indicadores.add_column(justify="center")

    sensacion = Group(
        Text("♨", style="bold bright_white"),
        Text("Sensación", style="dim"),
        Text(
            f'{clima_actual["sensacion_termica"]} °C',
            style="bold cyan"
        )
    )

    humedad = Group(
        Text("💧", style="bold bright_white"),
        Text("Humedad", style="dim"),
        Text(
            f'{clima_actual["humedad"]} %',
            style="bold cyan"
        )
    )

    viento = Group(
        Text("≋", style="bold bright_white"),
        Text("Viento", style="dim"),
        Text(
            f'{clima_actual["viento"]} km/h',
            style="bold cyan"
        )
    )

    indicadores.add_row(
        Align.center(sensacion),
        Align.center(humedad),
        Align.center(viento)
    )

    contenido_actual = Group(
        Align.center(ciudad),
        Align.center(temperatura),
        Align.center(descripcion),
        "",
        indicadores
    )

    panel_actual = Panel(
        contenido_actual,
        title="[bold bright_blue]WEATHER CONSOLE - HOY[/bold bright_blue]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    )

    pronostico_manana = mostrar_pronostico(
        clima["pronostico"][0],
        "MAÑANA"
    )

    pronostico_pasado = mostrar_pronostico(
        clima["pronostico"][1],
        "PASADO MAÑANA"
    )

    pronosticos = Table.grid(expand=True, padding=(0, 1))
    pronosticos.add_column(ratio=1)
    pronosticos.add_column(ratio=1)

    pronosticos.add_row(
        pronostico_manana,
        pronostico_pasado
    )

    consola.print(
        Group(
            panel_actual,
            pronosticos
        )
    )