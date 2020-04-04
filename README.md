# rasa chatbot on medical
这是一个基于Rasa构建的智能聊天助手，主要用于进行医疗健康相关问题的解答。

Rasa作为一个智能交互的框架非常适用于问答的聊天场景。本仓库使用借鉴了 Rasa Milk Tea Chatbot的方案，基于新的对话场景进行了处理。
https://github.com/BI4O/rasa_milktea_chatbot 可以参考这个库

另外本聊天后台的数据基于 QASystemOnmedicalKG的内容，在这个库中，作者使用Neo4j数据库，构建了基本的知识图谱。
库地址为：https://github.com/liuhuanyong/QASystemOnMedicalKG

# 本库做了什么
本库非常不好意思的融合了上一章节的两个库的技术，采用了拿来主义，通过rasa构建了一个聊天的场景。调用知识图谱作为后台数据源。


# 未来会继续做什么
会不断更新这个库，并且更加合理的调用不同的模型，提高准确率，也将通过更加详尽的文字，描述真正项目的构建过程。

# 怎么联系到我

Email：343152747@qq.com

If you have any question, please contact me by email or QQ.


