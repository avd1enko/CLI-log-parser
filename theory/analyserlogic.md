мы можем при помощи аргументов из терминала выбрать, какие анализаторы будут добавлены в список активных анализаторов, каждый из которых будет получать строку при помощи цикла for
```python
for line in file:
    parsed = parse_line(line)
    for analyzer in active_analyzers:
        analyzer.process(parsed)
```
```python
analyzers = []

if args.top_ips:
    analyzers.append(TopIPAnalyzer())

if args.errors_only:
    analyzers.append(ErrorFilter())

if args.methods:
    analyzers.append(MethodCounter())
```
Список анализаторов
1) Error Analyzer (--errors)
2) Method Analyzer (--methods)
3) Path heatmap Analyzer (--paths)
4) Time heatmap Analyzer (--timemap)
