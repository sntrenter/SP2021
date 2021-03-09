#lang racket/base
(println "Start")
(display "\n")
; Write a Racket function rem_second that takes
; a simple list as a parameter and returns a list 
;identical to the parameter except with the second 
;top-level element removed. If the given list does 
;not  have two elements, the function should return an empty list.


(define (rem_second l)
(cons (car l) (cddr l))
)

(define l1 (list 1 2 3 4 5 6))
(define l2 (list 1 (list 2 3 4) 3 4 5 6))
l1
(rem_second l1)
l2
(rem_second l2)




(println "end")