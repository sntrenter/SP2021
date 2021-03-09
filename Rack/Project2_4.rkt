#lang racket/base
(println "Start")
(display "\n")
;Write a function my_delete that takes two parameters:
; an atom and a list that contains a given atom (which may be a nested list). This 
;function will produce a list, identical to its parameter list, except with all
; occurrences of an atom parameter removed, no matter how deep they were. 
;The produced list should not have anything in place of the deleted atoms. 
;It is not necessary to validate input.


(define (my_delete list atom )
    (cond ((null? list) '()) 
            ((equal? (car list) atom) (my_delete (cdr list) atom)) 
            (else (cons (car list) (my_delete (cdr list) atom)))
    )
) 


(my_delete '(1 2 3 4 2 5) '2)
(my_delete '(a f c g f b) 'f)

(println "end")