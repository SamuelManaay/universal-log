# 🔊 Universal Logger for Python

Write logs in Python using styles from other programming languages like JavaScript, Java, C#, Bash, PHP, and more — without importing anything!

This tool injects popular log-style functions (like `console.log()`, `System.out.println()`, etc.) directly into Python's global scope via `sitecustomize.py`.

---

## 🚀 Features

- `console.log()` — JavaScript-style logging
- `System.out.println()` — Java-style logging
- `Console.WriteLine()` — C#-style logging
- `echo()` — PHP-style logging
- `puts()` and `println()` — Ruby-style / generic
- `fmt.Println()` — Go-style
- `sh_echo()` and `println_rust()` — Shell and Rust-like output
- Works everywhere without needing to import
- Optional Pylance/VS Code IntelliSense support

---

## 🧪 Example Usage

```python
Test_Text = "Hello World!"

console.log(Test_Text)
System.out.println("Java-style")
Console.WriteLine("C# style here")
echo("PHP-style echo")
puts("Ruby-style puts")
fmt.Println("Go-style println")
