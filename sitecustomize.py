import builtins
import sys
from typing import TYPE_CHECKING, Any

# JavaScript-style
class console:
    @staticmethod
    def log(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)

# Java-style
class System:
    class out:
        @staticmethod
        def println(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)

# C#-style
class Console:
    @staticmethod
    def WriteLine(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)

# Other styles
def echo(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)
def sh_echo(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)
def println(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)
def puts(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)
def println_rust(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)
def fmt_Println(*args: Any, **kwargs: Any) -> None: print(*args, **kwargs)

# Add to builtins
builtins.console = console  # type: ignore
builtins.System = System  # type: ignore
builtins.Console = Console  # type: ignore
builtins.echo = echo  # type: ignore
builtins.sh_echo = sh_echo  # type: ignore
builtins.println = println  # type: ignore
builtins.puts = puts  # type: ignore
builtins.println_rust = println_rust  # type: ignore
builtins.fmt = type("fmt", (), {"Println": staticmethod(fmt_Println)})  # type: ignore

# For Pylance type checking
if TYPE_CHECKING:
    from typing import Protocol
    class ConsoleProtocol(Protocol):
        @staticmethod
        def log(*args: Any, **kwargs: Any) -> None: ...
    
    class SystemProtocol(Protocol):
        class out:
            @staticmethod
            def println(*args: Any, **kwargs: Any) -> None: ...
    
    class DotNetConsoleProtocol(Protocol):
        @staticmethod
        def WriteLine(*args: Any, **kwargs: Any) -> None: ...
    
    console: ConsoleProtocol
    System: SystemProtocol
    Console: DotNetConsoleProtocol
    echo: Any
    sh_echo: Any
    println: Any
    puts: Any
    println_rust: Any
    fmt: Any

# Make available for direct import
sys.modules['universal_log'] = sys.modules[__name__]