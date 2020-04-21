# Device Registry Service
## Usage

- http://0.0.0.0:5000/alive    
**Il renverra simplement le text brut : "hello world".**


- http://0.0.0.0:5000/api/v1/conway/num    
**Il  prend en entrée un entier et il ressortira le n-ème terme de la suite de conway en texte brut.**

### Par exmeple :
http://0.0.0.0:5000/api/v1/conway/2    
**Il ressortira le 2-ème terme de la suite de conway.**     
    
http://0.0.0.0:5000/api/v1/conway/10    
**Il ressortira le 10-ème terme de la suite de conway.**
