# PyhopMT, uma versão multithread do planejador Pyhop

Baseado na versão 1.22 do Pyhop, desenvolvido por Dana nau.

----

Copyright 2013 Dana S. Nau - http://www.cs.umd.edu/~nau

Repositório da versão original: https://bitbucket.org/dananau/pyhop

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Pyhop é um planejador HTN simples escrito em Python. Ele funciona tanto no Python 2 quanto no 3.

Pyhop é de fácil implementação (menos de 150 linhas de código). Se você entender as ideias básicas do planejamento HTN ([esta apresentação](http://www.cs.umd.edu/~nau/papers/nau2013game.pdf) contém um resumo rápido), o Pyhop deve ser fácil de entender. Para exemplos de como usá-lo, veja os arquivos de exemplo que o acompanham.

----



A implementação corrente implementa uma versão multithread do Pyhop, bem como apresenta mais de um plano possível para um dado objetivo. Os arquivos dessa versão estão em pyhopmt.py e pyhopmtpool.py. Basta substituí-los nos exemplos. 
