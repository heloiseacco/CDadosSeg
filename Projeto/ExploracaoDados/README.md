<h3 align="center">
    Disciplina - ci1030-ERE2-CiênciaDeDados - PPGINF - UFPR 
</h3>

<h4 align="center">
  Heloise Acco Tives - Matrícula: 202000144019 <br />
  Roberta Samistraro Tomigian -  GRR - 20171631
  <br />
  Projeto de Mineração de Dados: Etapa de Exploração dos dados. 
</h4>

<h4>
1. Origem dos Dados
</h4>

<p>    
https://www.unb.ca/cic/datasets/darknet2020.html <br />
Descrever ........
</p>

<h4>
2. Descrição dos tipos de dados
</h4>

<p>  
    
- 85 atributos estruturam a tabela que contém 141.530 registros.

- 5 são textuais e 80 numéricos, conforme apresentado abaixo:

    
</p>

<h4>
3. Objetivo com dataset
</h4>
<p> 

Descobrir a partir da análise dos valores mínimos e máximos dos pacotes de entrada e saída
</p>
  

<h4>
4. Maneira de rotulação do dataset
</h4>



<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"><span style="font-weight:bold;color:#000;background-color:#FFF">Atributo</span></th>
    <th class="tg-0pky"><span style="font-weight:bold;color:#000">Tipo</span></th>
    <th class="tg-0pky"><span style="font-weight:bold;color:#000">Descrição</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow ID</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">ID de fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Src IP</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">IP Origem</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Src Port</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Porta Origem</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Dst IP</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">IP Destino</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Dst Port</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Porta Destino</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Protocol</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Protocolo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Timestamp</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0pky">Marca temporal</td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow Duration</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Duração do fluxo em microssegundos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Fwd Packet</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Pacotes totais enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Bwd packets</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Pacotes totais recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Length of Fwd Packet</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho total do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Length of Bwd Packet</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho total do pacote recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho máximo do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho mínimo do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho médio do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho do desvio padrão do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho máximo do pacote recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho mínimo do pacote recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho médio do pacote recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho do desvio padrão do pacote recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow Bytes/s</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de bytes de fluxo por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow Packets/s</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes de fluxo por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo médio entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo de desvio padrão entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo máximo entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo mínimo entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Total</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo total entre dois pacotes enviados enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo médio entre dois pacotes enviados enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo de desvio padrão entre dois pacotes enviados enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo máximo entre dois pacotes enviados enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo mínimo entre dois pacotes enviados enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Total</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo total entre dois pacotes enviados recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo médio entre dois pacotes enviados recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo de desvio padrão entre dois pacotes enviados recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo máximo entre dois pacotes enviados recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo mínimo entre dois pacotes enviados recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd PSH Flags</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira PSH foi definida em pacotes que viajam enviados (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd PSH Flags</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira PSH foi definida em pacotes que viajam na direção para trás (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd URG Flags</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira URG foi definida em pacotes que viajam enviados (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd URG Flags</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira URG foi definida em pacotes que viajam na direção para trás (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Header Length</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Total de bytes usados para cabeçalhos enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Header Length</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Total de bytes usados para cabeçalhos no sentido inverso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packets/s</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes encaminhados por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packets/s</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes inversos por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Comprimento mínimo de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Comprimento máximo de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Comprimento médio de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Comprimento do desvio padrão de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Variance</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Comprimento de variância de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">FIN Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com FIN</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">SYN Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com SYN</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">RST Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com RST</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">PSH Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com PSH</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">ACK Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com ACK</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">URG Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com URG</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">CWE Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com CWR</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">ECE Flag Count</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número de pacotes com ECE</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Down/Up Ratio</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Taxa de download e upload</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Average Packet Size</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho médio do pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Segment Size Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho médio observado enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Segment Size Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Taxa média do número de bytes em massa no sentido inverso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Bytes/Bulk Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Taxa média do número de bytes em massa enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet/Bulk Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Taxa média do número de pacotes em massa na direção direta</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Bulk Rate Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número médio de taxa em massa enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Bytes/Bulk Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Taxa média do número de bytes em massa no sentido inverso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet/Bulk Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Taxa média do número de pacotes em massa recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Bulk Rate Avg</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Número médio de taxa em massa recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Fwd Packets</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">O número médio de pacotes em um subfluxo enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Fwd Bytes</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">O número médio de bytes em um subfluxo enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Bwd Packets</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">O número médio de pacotes em um subfluxo recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Bwd Bytes</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">O número médio de bytes em um subfluxo recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">FWD Init Win Bytes</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">O número total de bytes enviados na janela inicial enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Init Win Bytes</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">O número total de bytes enviados na janela inicial recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Act Data Pkts</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Contagem de pacotes com pelo menos 1 byte de carga útil de dados TCP enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Seg Size Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tamanho mínimo do segmento observado enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo médio em que um fluxo estava ativo antes de ficar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo de desvio padrão em que um fluxo estava ativo antes de ficar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo máximo em que um fluxo ficou ativo antes de se tornar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo mínimo em que um fluxo esteve ativo antes de se tornar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Mean</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo médio em que um fluxo ficou ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Std</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo de desvio padrão em que um fluxo estava ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Max</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo máximo em que um fluxo ficou ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Min</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Tempo mínimo em que um fluxo ficou ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Label</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Rótulo 1</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000;background-color:#FFF">Label</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;color:#000">Rótulo 2</span></td>
  </tr>
</tbody>
</table>

<h4>
5. Colunas/atributos a serem mantidos e removidos. Por quê?
</h4>
<p> 
    
- O primeiro grupo de atributos excluídos foram os que se tratavam de resultados estatísticos calculados a partir de atributos originais de valores mínimos e máximos, ou seja, os atributos referentes ao cálculo de desvio padrão, média e variância. 
    
</p>  
  
  
