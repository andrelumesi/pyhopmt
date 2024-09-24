# PyhopMT, a multithreaded version of the Pyhop planner

Based on Pyhop version 1.22, developed by Dana Nau.

----

Copyright 2013 Dana S. Nau - http://www.cs.umd.edu/~nau

Repositório da versão original: https://bitbucket.org/dananau/pyhop

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Pyhop is a simple HTN planner written in Python. It works in both Python 2 and 3.

Pyhop was easy to implement (less than 150 lines of code), and if you understand the basic ideas of HTN planning ([this presentation](https://www.cs.umd.edu/~nau/papers/nau2013game.pdf) contains a quick summary), Pyhop should be easy to understand. For examples of how to use it, see the example files that come with it.

----



The current implementation provides a multithreaded version of Pyhop, as well as presenting more than one possible plan for a given goal. The files for this version are in pyhopmt.py and pyhopmtpool.py. Replace them in the examples.
