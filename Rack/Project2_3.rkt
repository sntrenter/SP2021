#lang racket/base
(println "Start")
(display "\n")
; Write a Racket function my_union that returns a union
; of two simple list parameters that represent sets.
; Remember that duplicate elements are not allowed in a set. 
;You are only allowed to use a program ‘membership.rkt’ from the folder 
;‘DrRacket’ under ‘Modules’; no other functions!


(define (my_union  a b)
  (cond ((null? b) a)
        ((member (car b) a)
         (my_union  a (cdr b)))
        (else (my_union  (cons (car b) a) (cdr b)))
    )
)

(my_union  '(1 3 4 5 2 7 ) '(2 5 8 9 0 4 2))
(my_union  '() '())
(my_union  '(1 3 4 5 2 7 ) '())




(println "end")