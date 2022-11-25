(define (my-filter func lst)   (
    cond
    ((null? lst) nil)
    (else (
      if (eq? (func (car lst)) '#t)
        (cons (car lst) (my-filter func (cdr lst)))
        (my-filter func (cdr lst))
    ))
  ))

(define (interleave s1 s2)   (
    cond
    ((or (null? s1) (null? s2)) (append s1 s2))
    (else (cons (car s1) (cons (car s2) (interleave (cdr s1) (cdr s2)))))
  ))

(define (accumulate merger start n term)
    (
    cond
        ((zero? n) start)
        (else (merger (term n) (accumulate merger start (- n 1) term)))
  ))

(define (func x y) (eq? x y))

(define (filter-same x func lst)   (
    cond
    ((null? lst) nil)
    (else (
      if (not (func x (car lst)))
        (cons (car lst) (filter-same x func (cdr lst)))
        (filter-same x func (cdr lst))
    ))
  ))


(define (no-repeats lst) 
    (
      cond
          ((null? lst) nil)
          (else (cons (car lst) (no-repeats (filter-same (car lst) func lst)))) 
    )
)


