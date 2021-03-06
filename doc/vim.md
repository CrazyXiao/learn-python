# vim简明指南

### 介绍

vim是一个类似于vi的著名的功能强大、高度可定制的文本编辑器，在vi的基础上改进和增加了很多特性。vim 相对于传统的 Unix vi 来说，取得了实质性进步。通常，vim 在 Linux 系统中是“vi”的符号链接（或别名）。在随后的讨论中，我们假定我们有一个叫做“vi”的程序，但它其实是 vim。

### 启动和退出 vim

要想启动 vim，只要简单地输入以下命令：

```
[me@linuxbox ~]$ vi
```

一个像这样的屏幕应该出现：

```
VIM - Vi Improved
....
```

正如我们之前操作 nano 时，首先要学的是怎样退出 vi。要退出 vi，输入下面的命令（注意冒号是命令的一部分）：

```
:q
```

shell 提示符应该重新出现。如果由于某种原因，vi 不能退出（通常因为我们对文件做了修改，却没有保存文件）。 通过给命令加上叹号，我们可以告诉 vi 我们真要退出 vi。（注意感叹号是命令的一部分）

```
:q!
```

小贴示：如果你在 vi 中“迷失”了，试着按下 Esc 键两次来回到普通模式。

### 编辑模式

再次启动 vi，这次传递给 vi 一个不存在的文件名。这也是用 vi 创建新文件的方法。

```
[me@linuxbox ~]$ rm -f foo.txt
[me@linuxbox ~]$ vi foo.txt
```

如果一切正常，我们应该获得一个像这样的屏幕：

```
....
"foo.txt" [New File]
```

每行开头的波浪号（"~"）表示那一行没有文本。这里我们有一个空文件。先别进行输入！

关于 vi ，第二重要的事是知晓vi 是一个模式编辑器。（第一件事是如何退出 vi ）vi 启动后会直接进入 命令模式。这种模式下，几乎每个按键都是一个命令，所以如果我们直接输入文本，vi 会发疯，弄得一团糟。

#### 插入模式

为了在文件中添加文本，我们需要先进入插入模式。按下"i"键进入插入模式。之后，我们应当 在屏幕底部看到如下的信息，如果 vi 运行在高级模式下（ vi 在兼容模式下不会显示这行信息）：

```
-- INSERT --
```

现在我们能输入一些文本了。试着输入这些文本：

```
The quick brown fox jumped over the lazy dog.
```

若要退出插入模式返回命令模式，按下 Esc 按键。

#### 保存我们的工作

为了保存我们刚才对文件所做的修改，我们必须在命令模式下输入一个 ex 命令。 通过按下":"键，这很容易完成。按下冒号键之后，一个冒号字符应该出现在屏幕的底部：

```
:
```

为了写入我们修改的文件，我们在冒号之后输入"w"字符，然后按下回车键：

```
:w
```

文件将会写入到硬盘，而且我们会在屏幕底部看到一行确认信息，就像这样：

```
"foo.txt" [New] 1L, 46C written
```

### 移动光标

当在 vi 命令模式下时，vi 提供了大量的移动命令，其中一些与 less 阅读器的相同。这里 列举了一些：

| 按键                | 移动光标                                          |
| ------------------- | ------------------------------------------------- |
| l or 右箭头         | 向右移动一个字符                                  |
| h or 左箭头         | 向左移动一个字符                                  |
| j or 下箭头         | 向下移动一行                                      |
| k or 上箭头         | 向上移动一行                                      |
| 0 (零按键)          | 移动到当前行的行首。                              |
| ^                   | 移动到当前行的第一个非空字符。                    |
| $                   | 移动到当前行的末尾。                              |
| w                   | 移动到下一个单词或标点符号的开头。                |
| W                   | 移动到下一个单词的开头，忽略标点符号。            |
| b                   | 移动到上一个单词或标点符号的开头。                |
| B                   | 移动到上一个单词的开头，忽略标点符号。            |
| Ctrl-f or Page Down | 向下翻一页                                        |
| Ctrl-b or Page Up   | 向上翻一页                                        |
| numberG             | 移动到第 number 行。例如，1G 移动到文件的第一行。 |
| G                   | 移动到文件末尾。                                  |

vi 中的许多命令都可以在前面加上一个数字，比方说上面提到的"G"命令。在命令之前加上一个 数字，我们就可以指定命令执行的次数。例如，命令"5j"将光标下移5行。

### 基本编辑

大多数编辑工作由一些基本的操作组成，比如说插入文本，删除文本和通过剪切和粘贴来移动文本。 vi，当然，有它独特方式来实现所有的操作。vi 也提供了撤销功能，但有些限制。如果我们按下“u” 按键，当在命令模式下，vi 将会撤销你所做的最后一次修改。当我们试着执行一些基本的 编辑命令时，这会很方便。

#### 追加文本

vi 有几种不同进入插入模式的方法。我们已经使用了 i 命令来插入文本。

让我们再次进入到我们的 foo.txt 文件：

```
The quick brown fox jumped over the lazy dog.
```

如果我们想要在这个句子的末尾添加一些文本，我们会发现 i 命令不能完成任务，因为我们不能把 光标移到行尾。vi 提供了追加文本的命令，明智地命名为"a"。如果我们把光标移动到行尾，输入"a", 光标就会越过行尾，同时 vi 会进入插入模式。这让我们能添加文本到行末：

```
The quick brown fox jumped over the lazy dog. It was cool.
```

记得按 Esc 键来退出插入模式。

因为我们几乎总是想要在行尾添加文本，所以 vi 提供了一个快捷键。光标将移动到行尾，同时 vi 进入输入模式。 它是"A"命令。试着用一下它，向文件添加更多行。

首先，使用"0"(零)命令，将光标移动到行首。现在我们输入"A"，然后输入下面这些文本：

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2
Line 3
Line 4
Line 5
```

再一次，按下 Esc 键退出插入模式。

正如我们所看到的， “A” 命令非常有用，因为它在进入到插入模式前，先将光标移到了行尾。

#### 打开一行

我们插入文本的另一种方式是“打开（open）”一行。这会在两行之间插入一个空白行，并且进入到插入模式。 这种方式有两个变体：

| 命令 | 打开行                 |
| ---- | ---------------------- |
| o    | 当前行的下方打开一行。 |
| O    | 当前行的上方打开一行。 |

我们可以演示一下：把光标移到"Line 3"上，再按下小 o 按键。

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2
Line 3

line 4
line 5
```

在第三行之下打开了新的一行，并且进入插入模式。按下 Esc，退出插入模式。按下 u 按键，撤销我们的修改。

按下大 O 按键在光标之上打开新的一行：

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2

Line 3
Line 4
Line 5
```

按下 Esc 按键，退出插入模式，并且按下 u 按键，撤销我们的更改。

#### 删除文本

正如我们所愿，vi 提供了各种删除文本到的方法，而且只需一或两个按键。首先， x 按键会删除光标位置的一个字符。可以在 x 命令之前带上一个数字，来指明要删除的字符个数。 d 按键更通用一些。跟 x 命令一样，d 命令之前可以带上一个数字，来指定要执行的删除次数。另外， d 命令之后总是带上一个移动命令，用来控制删除的范围。这里有些实例：

| 命令 | 删除的文本                               |
| ---- | ---------------------------------------- |
| x    | 当前字符                                 |
| 3x   | 当前字符及其后的两个字符。               |
| dd   | 当前行。                                 |
| 5dd  | 当前行及随后的四行文本。                 |
| dW   | 从光标位置开始到下一个单词的开头。       |
| d$   | 从光标位置开始到当前行的行尾。           |
| d0   | 从光标位置开始到当前行的行首。           |
| d^   | 从光标位置开始到文本行的第一个非空字符。 |
| dG   | 从当前行到文件的末尾。                   |
| d20G | 从当前行到文件的第20行。                 |

把光标放到第一行单词“It”之上。重复按下 x 按键直到删除剩下的部分。下一步，重复按下 u 按键 直到恢复原貌。

我们再次执行删除命令，这次使用 d 命令。还是移动光标到单词"It"之上，按下的 dW 来删除单词：

按下 d$删除从光标位置到行尾的文本：

```
The quick brown fox jumped over the lazy dog.
Line 2
Line 3
Line 4
Line 5
```

按下 dG 按键删除从当前行到文件末尾的所有行：

```
~
....
```

连续按下 u 按键三次，来恢复删除部分。

#### 剪切，复制和粘贴文本

这个 d 命令不仅删除文本，它还“剪切”文本。每次我们使用 d 命令，删除的部分被复制到一个 粘贴缓冲区中（看作剪切板）。过后我们执行小 p 命令把剪切板中的文本粘贴到光标位置之后， 或者是大 P 命令把文本粘贴到光标之前。

y 命令用来“拉”（复制）文本，和 d 命令剪切文本的方式差不多。这里有些把 y 命令和各种移动命令 结合起来使用的实例：

| 命令 | 复制的内容                               |
| ---- | ---------------------------------------- |
| yy   | 当前行。                                 |
| 5yy  | 当前行及随后的四行文本。                 |
| yW   | 从当前光标位置到下一个单词的开头。       |
| y$   | 从当前光标位置到当前行的末尾。           |
| y0   | 从当前光标位置到行首。                   |
| y^   | 从当前光标位置到文本行的第一个非空字符。 |
| yG   | 从当前行到文件末尾。                     |
| y20G | 从当前行到文件的第20行。                 |

我们试着做些复制和粘贴工作。把光标放到文本第一行，输入 yy 来复制当前行。下一步，把光标移到 最后一行（G），输入小写的 p 把复制的一行粘贴到当前行的下面：

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2
Line 3
Line 4
Line 5
The quick brown fox jumped over the lazy dog. It was cool.
```

和以前一样，u 命令会撤销我们的修改。这时光标仍位于文件的最后一行，输入大写的 P 命令把 所复制的文本粘贴到当前行之上：

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2
Line 3
Line 4
The quick brown fox jumped over the lazy dog. It was cool.
Line 5
```

试着执行上表中其他的一些 y 命令，了解小写 p 和大写 P 命令的行为。当你完成练习之后，把文件 恢复原样。

### 查找和替换

vi 能把光标移到搜索到的匹配项上。vi 不仅能在搜索一特定行，还能进行全文搜索。 它也可以在有或没有用户确认的情况下实现文本替换。

#### 查找一行

f 命令能搜索一特定行，并将光标移动到下一个匹配的字符上。例如，命令 fa 会把光标定位到同一行中 下一个出现的"a"字符上。在进行了一次行内搜索后，输入分号能重复这次搜索。

#### 查找整个文件

移动光标到下一个出现的单词或短语上，使用 / 命令。这个命令和我们之前在 less 程序中学到 的一样。当你输入/命令后，一个"/"字符会出现在屏幕底部。接下来，输入要查找的单词或短语， 按下回车。光标就会移动到下一个包含所查找字符串的位置。通过 n 命令来重复先前的查找。 这里有个例子：

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2
Line 3
Line 4
Line 5
```

移动光标到文件的第一行。输入：

```
/Line
```

然后敲回车。光标会移动到第二行。然后输入 n，这时光标移动到第三行。重复键入 n 命令，光标会 继续向下移动直到遍历所有的匹配项。至此我们只是通过输入单词和短语进行搜索，但 vi 支持正则 表达式，一种用于表达复杂文本的方法。我们将会在之后的章节中详细讲解正则表达式。

#### 全局查找和替代

vi 使用 ex 命令来执行查找和替代操作（vi 中叫做“替换”）。将整个文件中的单词“Line”更改为“line”， 输入以下命令：

```
:%s/Line/line/g
```

我们把这个命令分解为几个单独的部分，看一下每部分的含义：

| 条目       | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| :          | 冒号字符运行一个 ex 命令。                                   |
| %          | 指定要操作的行数。% 是一个快捷方式，表示从第一行到最后一行。另外，操作范围也 可以用 1,5 来代替（因为我们的文件只有5行文本），或者用 1,$ 来代替，意思是 “ 从第一行到文件的最后一行。” 如果省略了文本行的范围，那么操作只对当前行生效。 |
| s          | 指定操作。在这种情况下是，替换（查找与替代）。               |
| /Line/line | 查找类型与替代文本。                                         |
| g          | 这是“全局”的意思，意味着对文本行中所有匹配的字符串执行查找和替换操作。如果省略 g，则 只替换每个文本行中第一个匹配的字符串。 |

执行完查找和替代命令之后，我们的文件看起来像这样：

```
The quick brown fox jumped over the lazy dog. It was cool.
line 2
line 3
line 4
line 5
```

我们也可以指定一个需要用户确认的替换命令。通过添加一个"c"字符到这个命令的末尾，来完成 这个替换命令。例如：

```
:%s/line/Line/gc
```

这个命令会把我们的文件恢复先前的模样；然而，在执行每个替换命令之前，vi 会停下来， 通过下面的信息，来要求我们确认这个替换：

```
replace with Line (y/n/a/q/l/^E/^Y)?
```

Each of the characters within the parentheses is a possible choice as follows:

括号中的每个字符都是一个可能的选择，如下所示：

| 按键           | 行为                                                 |
| -------------- | ---------------------------------------------------- |
| y              | 执行替换操作                                         |
| n              | 跳过这个匹配的实例                                   |
| a              | 对这个及随后所有匹配的字符串执行替换操作。           |
| q or esc       | 退出替换操作。                                       |
| l              | 执行这次替换并退出。l 是 “last” 的简写。             |
| Ctrl-e, Ctrl-y | 分别是向下滚动和向上滚动。用于查看建议替换的上下文。 |

如果你输入 y，则执行这个替换，输入 n 则会导致 vi 跳过这个实例，而移到下一个匹配项上。

### 编辑多个文件

同时能够编辑多个文件是很有用的。你可能需要更改多个文件或者从一个文件复制内容到 另一个文件。通过 vi，我们可以打开多个文件来编辑，只要在命令行中指定要编辑的文件名。

```
vi file1 file2 file3...
```

我们先退出已经存在的 vi 会话，然后创建一个新文件来编辑。输入:wq 来退出 vi 并且保存了所做的修改。 下一步，我们将在家目录下创建一个额外的用来玩耍的文件。通过获取从 ls 命令的输出，来创建这个文件。

```
[me@linuxbox ~]$ ls -l /usr/bin > ls-output.txt
```

用 vi 来编辑我们的原文件和新创建的文件：

```
[me@linuxbox ~]$ vi foo.txt ls-output.txt
```

vi 启动，我们会看到第一个文件显示出来：

```
The quick brown fox jumped over the lazy dog. It was cool.
Line 2
Line 3
Line 4
Line 5
```

#### 文件之间切换

从这个文件切换下一个文件，使用这个 ex 命令：

```
:n
```

回到先前的文件使用：

```
:N
```

当我们从一个文件移到另一个文件时，如果当前文件没有保存修改，vi 会阻止我们切换文件， 这是 vi 强制执行的政策。在命令之后添加感叹号，可以强迫 vi 放弃修改而转换文件。

#### 打开另一个文件并编辑

在我们的当前的编辑会话里也能添加别的文件。ex 命令 :e (编辑(edit) 的简写) 紧跟要打开的文件名将会打开 另外一个文件。 让我们结束当前的会话回到命令行。

重新启动vi并只打开一个文件

```
[me@linuxbox ~]$ vi foo.txt
```

要加入我们的第二个文件，输入：

```
:e ls-output.txt
```

它应该显示在屏幕上。

注意：当文件由 ：e 命令加载，你将无法用 :n 或 :N 命令来切换文件。 

#### 插入整个文件到另一个文件

我们也可以把整个文件插入到我们正在编辑的文件中。看一下实际操作，结束 vi 会话，重新 启动一个只打开一个文件的 vi 会话：

```
[me@linuxbox ~]$ vi ls-output.txt
```

再一次看到我们的文件列表：

```
total 343700
-rwxr-xr-x 1 root root    31316  2007-12-05  08:58 [
```

移动光标到第三行，然后输入以下 ex 命令：

```
:r foo.txt
```

这个:r 命令（是"read"的简称）把指定的文件插入到光标位置之前。

### 保存工作

像 vi 中的其它操作一样，有几种不同的方法来保存我们所修改的文件。我们已经研究了:w 这个 ex 命令， 但还有几种方法，可能我们也觉得有帮助。

在命令模式下，输入 ZZ 就会保存并退出当前文件。同样地，ex 命令:wq 把:w 和:q 命令结合到 一起，来完成保存和退出任务。

这个:w 命令也可以指定可选的文件名。这个的作用就如"Save As..."。例如，如果我们 正在编辑 foo.txt 文件，想要保存一个副本，叫做 foo1.txt，那么我们可以执行以下命令：

```
:w foo1.txt
```

注意：当上面的命令以一个新名字保存文件时，它并没有更改你正在编辑的文件的名字。 如果你继续编辑，你还是在编辑文件 foo.txt，而不是 foo1.txt。

------

更多：[快乐的 Linux 命令行](https://github.com/billie66/TLCL/blob/gh-pages/book)



