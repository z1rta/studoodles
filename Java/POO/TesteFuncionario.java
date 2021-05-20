
public class TesteFuncionario {

	public static void main(String[] args) {
		Funcionario f1 = new Funcionario();
		f1.setNome("Nico Steppot");
		f1.setCpf("33333333333");
		f1.setSalario(1000);
		
		System.out.println(f1.getNome());
		System.out.println(f1.getBonificacao());
		
	}
}
