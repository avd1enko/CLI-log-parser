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