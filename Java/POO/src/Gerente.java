
public class Gerente extends Funcionario { //Gerente eh um funcionario
	
	private int senha;
	private String login;
	
	public void setLogin(String login) {
		this.login = login;
	}

	public void setSenha(int senha) {
		this.senha = senha;
	}
	
	public boolean autentica(int senha) {
		if(this.senha == senha) {
			return true;
		} else {
			return false;
		}
	}
	
	public boolean autentica(String login, int senha) { 	// É criado uma nova versão de um metódo, no caso o autentica
		if((this.login == login) && (this.senha == senha)) { // que variam na quantidade ou tipos de param. (SOBRECARGA!!)
			return true;
		} else {
			return false;
		}
	}
	
	public Gerente() { //Construtor
		
	}
	
	public double getBonificacao() {
		return super.getBonificacao() + super.getSalario(); // o super só pode ser usado quando o atributo está definido como "protected", 
							  								//	sendo assim, só sendo ussado pelos filhos da classe pai. (HERANÇA!!)
	}
	
}
	