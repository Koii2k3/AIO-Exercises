def exercise1(tp, fp, fn):
    # Check type
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return

    # Check value
    if tp < 1 or fp < 1 or fn < 1:
        print('tp and fp and fn must be greater than zero')
        return

    # Calculate
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))

    # Print
    print(f'Precision: {precision}\nRecall: {recall}\nF1-Score: {f1_score}')


exercise1(tp=2, fp=3, fn=4)
exercise1(tp='a', fp=3, fn=4)
exercise1(tp=2, fp='a', fn=4)
exercise1(tp=2, fp=3, fn='a')
exercise1(tp=2, fp=3, fn=0)
exercise1(tp=2.1, fp=3, fn=0)
