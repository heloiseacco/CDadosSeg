


<h3 align="center">
    Disciplina - ci1030-ERE2-CiênciaDeDados - PPGINF - UFPR 
</h3>

<h4 align="center">
  Heloise Acco Tives - Matrícula: 202000144019
  <br />
  Trabalho 2 - Parte 1: Análise de APKs
</h4>

<p>
    
- Obtenha ao menos 10 APKs de, no mínimo, três categorias diferentes (https://www.apkmirror.com/categories/) para compor seu dataset cru

- Para cada APK coletada, extraia o arquivo AndroidManifest.xml em um diretório "manifests", lembrando de identificar o arquivo resultante (por exemplo, se sua APK se chama 'BancoX-v01.apk', nomeie o manifesto como 'AndroidManifest_BancoX-v01.xml').

- Escreva um script em Python (ou um ipynb) que, dado um diretório como argumento de entrada, retorne a lista de permissões de cada AndroidManifest.xml sob a forma de um dicionário (chave: nome da APK, valor: lista de permissões). Exemplo de saída impressa no terminal desta parte do script:
</p>

<h4> Entradas Esperadas </h4>

Para uso no Google Colab: 
- Use o arquivo T2_Parte1.ipynb
- No primeiro bloco de código, carregue os arquivos de Manifesto das APKs (pasta manifest do repositório). Crie o diretório "manifests" no Colab e mova os arquivos para ele.

Para uso em ambiente desktop: 
- Use o arquivo t2_Parte1.py
- Certifique-se que o diretório "manifests" contendo arquivos de Manifesto de APKs foi baixado junto com o projeto. 


<h4> Orientações para execução </h4>

- Execute o código principal.
- O resultado apresentado será similar ao registrado no arquivo: T2_Parte1.ipynb - Demonstração de Resultado.pdf

