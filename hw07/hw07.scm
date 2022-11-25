(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
)

(define (caddr s) 
    (car (cdr (cdr s)))
)

(define (ordered? s) 
    (cond
        ((null? (cdr s)) #t)
        ((> (car s) (car (cdr s))) #f)
        (else (ordered? (cdr s)))
    )
)

(define (square x) (* x x))

(define (pow base exp) 
    (cond
        ((= exp 0) 1)
        ((= base 1) 1)
        ((= exp 1) base)
        ((even? exp) (pow (square base) (/ exp 2)))
        (else (* base (pow base (- exp 1))))
    )
)


(define (label tree)
    (car tree)
)

(define (branches tree)
    (cdr tree)
)

(define (map-fn fn lst)
    (
        cond
            ((null? lst) '())
            (else (cons (fn (car lst)) (map-fn fn (cdr lst) ) ) )
    )
)

(define (tree-sum tree)
    'YOUR-CODE-HERE
)

(define (sum lst)
    'YOUR-CODE-HERE
)

(define t (make-tree 1 (list (make-tree 2 '()) (make-tree 3 '()))))
(expect (tree-sum t) 6)
