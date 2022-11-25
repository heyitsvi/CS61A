(define (over-or-under num1 num2) (
        cond
            ((< num1 num2) -1)
            ((= num1 num2) 0)
            (else 1) 
    )
)

(define (make-adder num) 
    (lambda (inc) (+ inc num))
)

(define (composed f g) 
    (lambda (num) (f (g num)))
)

(define lst 'YOUR-CODE-HERE)

(define (remove item lst) 
    (
        filter (lambda (x) (= x item)) lst
    )
)

