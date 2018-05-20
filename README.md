# Chinese_txt_similarity
## 中文文本相似度算法实现
## 包括 simhash、余弦相似度、编辑距离

### 1、Simhash相似度算法
simhash是一种局部敏感hash。什么叫局部敏感呢，假定A、B具有一定的相似性，在hash之后，仍然能保持这种相似性，就称之为局部敏感hash。
利用结巴分词得到一个文档的分词集合，然后通过hash的方法，把上述得到的分词集合hash成一串二进制，这样我们直接对比二进制数，看其相似性就可以得到两篇文档的相似性，在查看相似性的时候我们采用海明距离，即在对比二进制的时候，我们看其有多少位不同，就称海明距离为多少。在这里，我是将文章simhash得到一串64位的二进制，一般取海明距离为3作为阈值，即在64位二进制中，只有三位不同，我们就认为两个文档是相似的。当然了，这里可以根据自己的需求来设置阈值。

就这样，我们把一篇文档用一个二进制代表了，也就是把一个文档hash之后得到一串二进制数的算法，称这个hash为simhash。

具体simhash步骤如下：

（1）将文档分词，得到文章的分词集合。

（2）对其中的词，进行普通的哈希之后得到一个64为的二进制，词的hash集合。

（3）根据（2）中得到一串二进制数（hash）中相应位置是1是0，对相应位置取正值weight和负值weight。例如一个词进过（2）得到（010111：1）进过步骤（3）之后可以得到列表[-1,1,-1,1,1,1]，即对一个文档，我们可以得到（词集合长度）个长度为64的列表[weight，-weight…weight]。
这里考虑的全部分词，所以权重都是1。

（4）对（3）中词集合进行列向累加得到一个列表。如[-1,1,-1,1,1,1]、[-1,-1,-1,1,-1,1]、[1,-1,-1,1,1,1]进行列向累加得到[-1，-1，-3，3，1，3]，这样，我们对一个文档得到，一个长度为64的列表。

（5）对（4）中得到的列表中每个值进行判断，当为负值的时候去0，正值取1。例如，[-1，-1，-3，3，1，3]得到000111，这样，我们就得到一个文档的simhash值了。

（6）计算相似性。连个simhash取异或，看其中1的个数是否超过3。超过3则判定为不相似，小于等于3则判定为相似。

### 2、余弦相似度算法

（1）使用jieba分词，获取两篇文章的分词；
（2）每篇文章的分词合并成一个集合，计算每篇文章对于这个集合中的词的词频（为了避免文章长度的差异，可以使用相对词频）；
（3）生成两篇文章各自的词频向量；
（4）计算两个向量的余弦相似度，值越大就表示越相似。

### 3、编辑距离
所谓文本的编辑距离，是指从一个文本变成另一个文本所需要的做小操作数。这些操作一般包括字符的插入、删除和替换。这个概念是俄罗斯科学家在1965年提出来的。

编辑距离的算法可以概括以下：定义一个编辑距离的函数 editText（i,j）表示从从长度为i的字符串变到长度为j的字符串所需要的最小操作数。这个问题可以用动态规划的方法来求解。概括为以下几点：

if (i == 0 && j == 0) edit(i, j) = 0;
if (i == 0 && j > 0) edit(i, j) = j;
if (i > 0 && j == 0) edit(i, j) = i;
if (i >= 1 && j >= 1) edit(i, j) == min( edit(i - 1, j) + 1, edit(i, j - 1) + 1, edit(i - 1, j-1) + f(i,j) ); 其中当字符串A的第i个字符和字符串B的第j个字符相同时，f(i,j) 为零，否则为一。