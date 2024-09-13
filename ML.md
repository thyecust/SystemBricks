## Transformer

https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)

[Handmade Transformer predicting the sequence "aabaabaabaab..."](https://vgel.me/posts/handmade-transformer/)

```python
def complete(s, max_new_tokens=10):
  tokens = tokenize(s)
  while len(tokens) < len(s) + max_new_tokens:
    logits = gpt(np.array(tokens[-5:]), **MODEL)
    probs = softmax(logits)
    pred = np.argmax(probs[-1]) # greedy sample, but temperature sampling would give the same results in our case
    tokens.append(pred)
  return s + " :: " + "".join(untok(t) for t in tokens[len(s):])

print(complete("a")) # a :: baabaabaab
print(complete("ba")) # ba :: abaabaabaa
print(complete("abaab")) # abaab :: aabaabaaba
```