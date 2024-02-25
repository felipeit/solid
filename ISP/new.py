from abc import ABC, abstractmethod

# Interface segregada para Desenvolvedor
class Desenvolvedor(ABC):
    @abstractmethod
    def implementar_funcionalidade(self):
        pass

# Interface segregada para Scrum Master
class ScrumMaster(ABC):
    @abstractmethod
    def facilitar_reunioes(self):
        pass

# Interface segregada para Product Owner
class ProductOwner(ABC):
    @abstractmethod
    def priorizar_backlog(self):
        pass

# Implementação para Desenvolvedor
class DesenvolvedorScrum(Desenvolvedor):
    def implementar_funcionalidade(self):
        print("Desenvolvedor está implementando uma funcionalidade.")

# Implementação para Scrum Master
class ScrumMasterScrum(ScrumMaster):
    def facilitar_reunioes(self):
        print("Scrum Master está facilitando reuniões do Scrum.")

# Implementação para Product Owner
class ProductOwnerScrum(ProductOwner):
    def priorizar_backlog(self):
        print("Product Owner está priorizando o backlog do Scrum.")

# Cliente que interage com um Desenvolvedor
def interagir_com_desenvolvedor(dev: Desenvolvedor):
    dev.implementar_funcionalidade()

# Cliente que interage com um Scrum Master
def interagir_com_scrum_master(scrum_master: ScrumMaster):
    scrum_master.facilitar_reunioes()

# Cliente que interage com um Product Owner
def interagir_com_product_owner(product_owner: ProductOwner):
    product_owner.priorizar_backlog()

# Exemplo de uso
desenvolvedor_scrum = DesenvolvedorScrum()
scrum_master_scrum = ScrumMasterScrum()
product_owner_scrum = ProductOwnerScrum()

interagir_com_desenvolvedor(desenvolvedor_scrum)
interagir_com_scrum_master(scrum_master_scrum)
interagir_com_product_owner(product_owner_scrum)
