import platform
import cpuinfo
import socket
import os

class SystemInfo:
    """
    A class for retrieving various system information.

    Attributes:
        system (str): The name of the operating system (e.g. 'Windows', 'Linux').
        node (str): The hostname of the computer.
        release (str): The release of the operating system.
        version (str): The version of the operating system.
        machine (str): The machine type (e.g. 'x86_64', 'AMD64').
        cpu_info (str): The CPU-related informations.
        ip_address (str): The IP address of the computer.
        username (str): The current username.

    Methods:
        to_json_list(): Returns a JSON representation of the SystemInfo instance.
    """

    def __init__(self) -> None :
        """Initializes the SystemInfo instance and retrieves system information."""
        self._system = platform.system()
        self._node = platform.node()
        self._release = platform.release()
        self._version = platform.version()
        self._machine = platform.machine()
        self._cpu_info = CPUInfo(cpuinfo.get_cpu_info())
        self._ip_address = socket.gethostbyname(socket.gethostname())
        self._username = os.getlogin()

    @property
    def system(self) -> str :
        """Returns the name of the operating system."""
        return self._system

    @property
    def node(self) -> str :
        """Returns the hostname of the computer."""
        return self._node

    @property
    def release(self) -> str :
        """Returns the release of the operating system."""
        return self._release

    @property
    def version(self) -> str :
        """Returns the version of the operating system."""
        return self._version

    @property
    def machine(self) -> str :
        """Returns the machine type."""
        return self._machine

    @property
    def cpu_info(self) -> str :
        """Returns the CPU-related informations."""
        return self._cpu_info

    @property
    def ip_address(self) -> str :
        """Returns the IP address of the computer."""
        return self._ip_address

    @property
    def username(self) -> str :
        """Returns the current username."""
        return self._username
    
    def __str__(self) -> str :
        """Returns a string representation of the SystemInfo instance."""
        return f"""System: {self.system} {self.release} {self.version} {self.machine} {self.node} {self.ip_address} {self.username} {self.cpu_info}"""
    
    def to_json_list(self) -> list :
        """Returns a JSON representation of the SystemInfo instance."""
        return [
            {
                "label": "Operating System",
                "value": self.system,
            },
            {
                "label": "Release",
                "value": self.release,
            },
            {
                "label": "Version",
                "value": self.version,
            },
            {
                "label": "Machine",
                "value": self.machine,
            },
            {
                "label": "Node",
                "value": self.node,
            },
            {
                "label": "IP Address",
                "value": self.ip_address,
            },
            {
                "label": "Username",
                "value": self.username,
            }
        ]

class CPUInfo:
    """
    A class that stores information about the CPU.

    Attributes:
        python_version (str): The version of Python.
        arch (str): The architecture of the CPU.
        processor (str): The name of the processor.
        hz_advertized (str): The advertised frequency of the processor.
        hz_actual (str): The actual frequency of the processor.

    Methods:
        to_json_list(): Returns a JSON representation of the CPUInfo instance.
    """

    def __init__(self, cpu_info) -> None :
        """
        Initializes the CPUInfo instance and retrieves CPU information.
        
        Args:
            cpu_info (str): Information about the CPU of the computer.
        """
        self._python_version = cpu_info["python_version"]
        self._arch = cpu_info["arch"]
        self._processor = cpu_info["brand_raw"]
        self._hz_advertized = cpu_info["hz_advertised_friendly"]
        self._hz_actual = cpu_info["hz_actual_friendly"]

    @property
    def python_version(self) -> str :
        """Returns the version of Python."""
        return self._python_version
    
    @property
    def arch(self) -> str :
        """Returns the architecture of the CPU."""
        return self._arch
    
    @property
    def processor(self) -> str :
        """Returns the name of the processor."""
        return self._processor
    
    @property
    def hz_advertized(self) -> str :
        """Returns the advertised frequency of the processor."""
        return self._hz_advertized
    
    @property
    def hz_actual(self) -> str :
        """Returns the actual frequency of the processor."""
        return self._hz_actual
    
    def __str__(self) -> str :
        """Returns a string representation of the CPUInfo instance."""
        return f"""CPU: {self.python_version} {self.arch} {self.processor} {self.hz_advertized} {self.hz_actual}"""
    
    def to_json_list(self) -> list :
        """Returns a JSON representation of the CPUInfo instance."""
        return [
            {
                "label": "Python Version",
                "value": self.python_version,
            },
            {
                "label": "Architecture",
                "value": self.arch,
            },
            {
                "label": "Processor",
                "value": self.processor,
            },
            {
                "label": "Advertized Frequency",
                "value": self.hz_advertized,
            },
            {
                "label": "Actual Frequency",
                "value": self.hz_actual,
            }
        ]