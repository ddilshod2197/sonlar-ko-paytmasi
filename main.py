def juft_toq_sonlar(ro'yhat):
    juft_sonlar = [son for son in ro'yhat if son % 2 == 0]
    toq_sonlar = [son for son in ro'yhat if son % 2 != 0]
    return juft_sonlar, toq_sonlar

ro'yhat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar, toq_sonlar = juft_toq_sonlar(ro'yhat)

print("Juft sonlar:", juft_sonlar)
print("To'q sonlar:", toq_sonlar)
```

```python
def juft_toq_sonlar(ro'yhat):
    return [son for son in ro'yhat if son % 2 == 0], [son for son in ro'yhat if son % 2 != 0]

ro'yhat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar, toq_sonlar = juft_toq_sonlar(ro'yhat)

print("Juft sonlar:", juft_sonlar)
print("To'q sonlar:", toq_sonlar)
