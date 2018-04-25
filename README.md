# Finding Barcenas
This project was made for the subject of Learning and automatic reasoning in University of Lleida (UDL).

Subject directed by Dr.Ramón Béjar Torres.

## Goal
The goal of this work is to develop an intelligent agent for the Barcenas World

## Input
1. The dimension of the world (the value of n for the n × n Barcenas World)
2. A sequence of l steps with their smell, Mariano and Cospedal readings of this form:

        [x1, y1,s1, ma1, ca1], [x2, y2,s2, ma2, ca2], ..., [xl, yl,sl, mal, cal]
        
    where [xt, yt,st, mat, cat,rat] indicates that at time step t:
    
    (a) the agent moves to position (x, y).
    
    (b) the smell sensor reads the value st, that can be either 1 (it smells like hell in xt , yt) or 0 (it does not smell in xt, yt).
    
    (c) if the agent finds Mariano at (x, y), his answer to the question Where is Barcenas ? will be in mat and will be either 1 (is on my left) or 0 (is on my right). If Mariano is not found at that time t mat will be -1.
    
    (d) if the agents finds Cospedal at (x, y), her answer to the question Is Mariano lying ? will be in cat and will be either 1 (true) or 0 (false). If Cospedal is not found at that time t cat will be -1.

## Built With
[Python](https://www.python.org/) - Primary Language, used to create the code in Prolog

[SWI-Prolog](http://www.swi-prolog.org/) - Result of the execution of the python program and the actual program that will do the job.

## Authors

* **Jordi Onrubia** - * Programmer * - [JordiROP](https://github.com/JordiROP)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
