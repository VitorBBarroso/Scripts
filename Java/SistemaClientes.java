import java.util.ArrayList;
import java.util.Scanner;

class Cliente {
    int id;
    String nome;
    String email;
    String telefone;

    public Cliente(int id, String nome, String email, String telefone) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.telefone = telefone;
    }
}

public class SistemaClientes {
    private static final ArrayList<Cliente> clientes = new ArrayList<>();
    private static int proximoId = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n===== Sistema de Gerenciamento de Clientes =====");
            System.out.println("1. Adicionar Cliente");
            System.out.println("2. Listar Clientes");
            System.out.println("3. Atualizar Cliente");
            System.out.println("4. Deletar Cliente");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1 -> adicionarCliente(scanner);
                case 2 -> listarClientes();
                case 3 -> atualizarCliente(scanner);
                case 4 -> deletarCliente(scanner);
                case 5 -> System.out.println("Saindo...");
                default -> System.out.println("Opção inválida!");
            }
        } while (opcao != 5);

        scanner.close();
    }

    private static void adicionarCliente(Scanner scanner) {
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        System.out.print("Email: ");
        String email = scanner.nextLine();
        System.out.print("Telefone: ");
        String telefone = scanner.nextLine();

        Cliente cliente = new Cliente(proximoId++, nome, email, telefone);
        clientes.add(cliente);
        System.out.println("Cliente adicionado com sucesso!");
    }

    private static void listarClientes() {
        System.out.println("\n===== Lista de Clientes =====");
        if (clientes.isEmpty()) {
            System.out.println("Nenhum cliente cadastrado.");
        } else {
            for (Cliente c : clientes) {
                System.out.println("ID: " + c.id + " | Nome: " + c.nome + " | Email: " + c.email + " | Telefone: " + c.telefone);
            }
        }
    }

    private static void atualizarCliente(Scanner scanner) {
        System.out.print("ID do cliente para atualizar: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        Cliente cliente = buscarClientePorId(id);
        if (cliente != null) {
            System.out.print("Novo Nome: ");
            cliente.nome = scanner.nextLine();
            System.out.print("Novo Email: ");
            cliente.email = scanner.nextLine();
            System.out.print("Novo Telefone: ");
            cliente.telefone = scanner.nextLine();

            System.out.println("Cliente atualizado com sucesso!");
        } else {
            System.out.println("Cliente não encontrado.");
        }
    }

    private static void deletarCliente(Scanner scanner) {
        System.out.print("ID do cliente para deletar: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        Cliente cliente = buscarClientePorId(id);
        if (cliente != null) {
            clientes.remove(cliente);                                   
            System.out.println("Cliente deletado com sucesso!");
        } else {
            System.out.println("Cliente não encontrado.");
        }
    }

    private static Cliente buscarClientePorId(int id) {
        for (Cliente c : clientes) {
            if (c.id == id) {
                return c;
            }
        }
        return null;
    }
}
