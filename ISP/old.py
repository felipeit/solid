from abc import ABC, abstractmethod

class MembroTimeSCRUM(ABC):
    
    @abstractmethod
    def priorizar_backlog():...
    
    @abstractmethod
    def blindar_time():...

    @abstractmethod
    def implementar_funcionalidade():...

class Dev(MembroTimeSCRUM):
    def priorizar_backlog():...

    def blindar_time():...

    def implementar_funcionalidade():...

class ScrumMaster(MembroTimeSCRUM):
    def priorizar_backlog():...

    def blindar_time():...

    def implementar_funcionalidade():...

class ProductOwner(MembroTimeSCRUM):
    def priorizar_backlog():...

    def blindar_time():...

    def implementar_funcionalidade():...
