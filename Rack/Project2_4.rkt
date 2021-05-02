#lang racket/base
;(define a 1)
;(define x 1)
;(define b 1)
;(define y 1)
;(/ (sqrt (+ (sin ((- (* 3 x) 1))(* 4 a)))(- (* b b)((tan y))))


;two way selection 
;return '(123)
;when first element of a_list is the atom 'a

(define a_list ('a 2 3))

(car a_list)

(if 
(eqv? (car a_list) 'a)
'(1 2 3)
'()
)
