#lang racket/base

(println "Start")
(display "\n")
;//In the beginning of each part of this problem, introduce a named value pi, which is 3.1416. 
;You will have to write a function my_calc that takes two numerical parameters. 
; If the first parameter is 1, calculate the area of a circle,
;     whose radius equals the second parameter of the function.
; If the first parameter is 2,
;     calculate the volume of the sphere, whose radius equals the second parameter of the function.
; For other values of the first parameter or for a non-positive second parameter return a false Boolean value.
;

;1.
(define pi 3.1416)
;2 way
(define (my_calc n x)
(if (eqv? n 1)
 (area x)
(if (eqv? n 2)
    (volume x)
    #f)
)
)




(define (area x)
(* pi (* x x))
)

(define (volume x)
(* (* (* (* (/ 4 3) pi) x) x) x)
)



(my_calc 1 2)
(my_calc 2 2)
(my_calc 3 2)


(println "end")