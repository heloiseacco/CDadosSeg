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

- 5 são textuais e 80 numéricos, conforme apresentado na tabela da seção 4. 

    
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

Os rótulos dos atributos do dataset obtido foram colocados na tabela abaixo, juntamente com a identificação do tipo de dados (textual e numérico) e uma descrição sobre o que os dados se referem. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:bold;color:#000;background-color:#FFF">Id</span></th>
    <th class="tg-0lax"><span style="font-weight:bold;color:#000;background-color:#FFF">Atributo</span></th>
    <th class="tg-0lax"><span style="font-weight:bold;color:#000">Tipo</span></th>
    <th class="tg-0lax"><span style="font-weight:bold;color:#000">Descrição</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">1</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow ID</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">ID do fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">2</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Src IP</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">IP de Origem</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">3</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Src Port</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Porta de Origem</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">4</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Dst IP</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">IP de Destino</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">5</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Dst Port</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Porta de Destino</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">6</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Protocol</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Protocolo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">7</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Timestamp</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0lax">Marca temporal</td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">8</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow Duration</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Duração do fluxo em microssegundos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">9</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Fwd Packet</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Total de Pacotes enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">10</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Bwd packets</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Total de Pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">11</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Length of Fwd Packet</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho total do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">12</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Total Length of Bwd Packet</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho total do pacote recebido</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">13</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho máximo do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">14</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho mínimo do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">15</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho médio do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">16</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet Length Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor so desvio padrão do pacote enviado</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">17</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho máximo dos pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">18</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho mínimo dos pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">19</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho médio dos pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">20</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet Length Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor do desvio padrão dos pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">21</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow Bytes/s</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de bytes do fluxo por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">22</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow Packets/s</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes de fluxo por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">23</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo médio entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">24</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor do desvio padrão entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">25</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo máximo entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">26</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Flow IAT Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo mínimo entre dois pacotes enviados no fluxo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">27</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Total</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo total entre dois pacotes enviados enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">28</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo médio entre dois pacotes enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">29</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor do desvio padrão entre dois pacotes enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">30</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo máximo entre dois pacotes enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">31</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd IAT Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo mínimo entre dois pacotes enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">32</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Total</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo total entre dois pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">33</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo médio entre dois pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">34</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor do desvio padrão entre dois pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">35</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo máximo entre dois pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">36</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd IAT Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo mínimo entre dois pacotes recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">37</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd PSH Flags</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira PSH foi definida em pacotes que foram enviados (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">38</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd PSH Flags</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira PSH foi definida em pacotes que foram recebidos (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">39</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd URG Flags</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira URG foi definida em pacotes que foram enviados (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">40</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd URG Flags</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de vezes que a bandeira URG foi definida em pacotes que foram recebidos (0 para UDP)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">41</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Header Length</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Total de bytes usados para cabeçalhos enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">42</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Header Length</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Total de bytes usados para cabeçalhos recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">43</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packets/s</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes enviados por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">44</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packets/s</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes recebidos por segundo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">45</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Comprimento mínimo de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">46</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Comprimento máximo de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">47</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Comprimento médio de um pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">48</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valoe do desvio padrão do comprimento dos pacotes</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">49</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Packet Length Variance</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor da variância do comprimentos dos pacotes</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">50</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">FIN Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com FIN</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">51</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">SYN Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com SYN</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">52</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">RST Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com RST</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">53</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">PSH Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com PSH</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">54</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">ACK Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com ACK</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">55</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">URG Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com URG</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">56</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">CWE Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com CWR</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">57</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">ECE Flag Count</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número de pacotes com ECE</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">58</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Down/Up Ratio</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Taxa de download e upload</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">59</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Average Packet Size</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho médio do pacote</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">60</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Segment Size Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho médio observado enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">61</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Segment Size Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Taxa média do número de bytes em massa recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">62</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Bytes/Bulk Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Taxa média do número de bytes em massa enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">63</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Packet/Bulk Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Taxa média do número de pacotes em massa enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">64</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Bulk Rate Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número médio de taxa em massa enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">65</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Bytes/Bulk Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Taxa média do número de bytes em massa recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">66</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Packet/Bulk Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Taxa média do número de pacotes em massa recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">67</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Bulk Rate Avg</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número médio de taxa em massa recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">68</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Fwd Packets</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número médio de pacotes em um subfluxo enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">69</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Fwd Bytes</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número médio de bytes em um subfluxo enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">70</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Bwd Packets</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número médio de pacotes em um subfluxo recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">71</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Subflow Bwd Bytes</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número médio de bytes em um subfluxo recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">72</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">FWD Init Win Bytes</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número total de bytes enviados na janela inicial enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">73</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Bwd Init Win Bytes</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Número total de bytes enviados na janela inicial recebidos</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">74</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Act Data Pkts</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Contagem de pacotes com pelo menos 1 byte de carga útil de dados TCP enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">75</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Fwd Seg Size Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tamanho mínimo do segmento observado enviados</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">76</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo médio em que um fluxo estava ativo antes de ficar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">77</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valoe do desvio padrão em que um fluxo estava ativo antes de ficar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">78</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo máximo em que um fluxo ficou ativo antes de se tornar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">79</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Active Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo mínimo em que um fluxo esteve ativo antes de se tornar ocioso</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">80</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Mean</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo médio em que um fluxo ficou ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">81</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Std</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Valor do desvio padrão em que um fluxo estava ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">82</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Max</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo máximo em que um fluxo ficou ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">83</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Idle Min</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Numérico</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Tempo mínimo em que um fluxo ficou ocioso antes de se tornar ativo</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">84</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Label</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Rótulo 1</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">85</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000;background-color:#FFF">Label</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Textual</span></td>
    <td class="tg-0lax"><span style="font-weight:normal;color:#000">Rótulo 2</span></td>
  </tr>
</tbody>
</table>

<h4>
5. Colunas/atributos a serem mantidos e removidos. Por quê?
</h4>
<p> 
    
- O primeiro grupo de atributos excluídos foram os que se tratavam de resultados estatísticos calculados a partir de atributos originais de valores mínimos e máximos, ou seja, os atributos referentes ao cálculo de desvio padrão, média e variância. 
    
</p>  
  
  
