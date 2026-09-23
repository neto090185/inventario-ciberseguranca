import os
import json
from enum import Enum

# --- REQUISITO 2: Estrutura de dados de enumeração para os tipos de ativos ---
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SISTEMA_WEB = 4

ARQUIVO_BD = "base_ativos.txt"

def carregar_dados():
    """Carrega os dados do arquivo de texto."""
    if not os.path.exists(ARQUIVO_BD):
        return {}
    try:
        with open(ARQUIVO_BD, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return {}

def salvar_dados(dados):
    """Salva os dados no arquivo de texto."""
    with open(ARQUIVO_BD, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# --- REQUISITO 3: Função de cadastro de ativo ---
def cadastrar_ativo():
    print("\n--- CADASTRO DE NOVO ATIVO ---")
    dados = carregar_dados()
    
    # Tratamento de erro para o Identificador (deve ser inteiro)
    while True:
        try:
            id_ativo = int(input("Identificador único (ID numérico): "))
            if str(id_ativo) in dados:
                print("Erro: Já existe um ativo cadastrado com este ID.")
                continue
            break
        except ValueError:
            print("Erro: O ID deve ser um número inteiro. Tente novamente.")

    # Validação de campos vazios
    nome = input("Nome ou Hostname: ").strip()
    while not nome:
        print("Erro: O nome não pode ficar vazio.")
        nome = input("Nome ou Hostname: ").strip()

    responsavel = input("Responsável pelo ativo: ").strip()
    setor = input("Setor ou Localização: ").strip()

    # Seleção do Tipo de Ativo
    print("\nTipos de Ativos Disponíveis:")
    for tipo in TipoAtivo:
        print(f"[{tipo.value}] {tipo.name.replace('_', ' ')}")
    
    while True:
        try:
            tipo_opcao = int(input("Escolha o código do tipo de ativo: "))
            tipo_ativo = TipoAtivo(tipo_opcao).name
            break
        except ValueError:
            print("Erro: Opção inválida. Digite o número correspondente ao tipo.")

    # Inserção de vulnerabilidades
    vulnerabilidades = []
    print("\nCadastro de Vulnerabilidades (deixe em branco e pressione Enter para finalizar):")
    while True:
        vuln = input("- Descrição da vulnerabilidade: ").strip()
        if not vuln:
            break
        vulnerabilidades.append(vuln)

    # Montando o dicionário do ativo
    novo_ativo = {
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo_ativo,
        "vulnerabilidades": vulnerabilidades
    }

    # Salvando no "banco de dados"
    dados[str(id_ativo)] = novo_ativo
    salvar_dados(dados)
    print(f"\nSucesso: Ativo '{nome}' cadastrado com sucesso!")

# --- REQUISITO 1: Menu textual com tratamento de erros ---
def exibir_menu():
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE INVENTÁRIO DE CIBERSEGURANÇA")
        print("="*40)
        print("1. Cadastrar Ativo de TI (Create)")
        print("2. Sair do Sistema")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_ativo()
        elif opcao == '2':
            print("Encerrando o sistema...")
            break
        else:
            print("Erro: Comando inválido. Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    exibir_menu()   