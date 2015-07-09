#!/usr/bin/env python


class Element(object):

    tag = ""
    indent = '\t'

    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    def append(self, new_text):
        self.content += str(new_text) #Used str() to fix TypeError

    def render(self, f, indent = ""):
        f.write('<>\n' + self.indent + self.content + '\n</>')


class Body(Element):

    def __init__(self):
        Element.__init__(self, 'Body', '')


class Html(Element):

    def __init__(self):
        Element.__init__(self, 'Html', '')


class P(Element):

    def __init__(self, content):
        Element.__init__(self, 'P', content)








    # indent = '    '

    # def __init__(self, tag, content):
    #     self.tag = tag
    #     self.content = ''
    #     self.childElements = []
    #     self.append(content)

    # def append(self, content):
    #     if isinstance(content, Element):
    #         self.childElements.append(content)
    #     else:
    #         self.content += content

    # def render(self, file_out, indent = ""):
    #     file_out.write(indent + '<' + self.tag + '>\n')
    #     for child in self.childElements:
    #         child.render(file_out, indent + Element.indent)
    #     if(self.content != ''):
    #         file_out.write(indent + Element.indent + self.content + '\n')
    #     file_out.write(indent + '</' + self.tag + '>')
    #     if(indent != ''):
    #         file_out.write('\n')




# class Html(Element):

#     def __init__(self):
#         Element.__init__(self, 'html', '')


# class Body(Element):

#     def __init__(self):
#         Element.__init__(self, 'body', '')


# class P(Element):

#     def __init__(self, content):
#         Element.__init__(self, 'p', content)

# class Head(Element):

#     def __init__(self):
#         Element.__init__(self, 'head', '')


# class OneLineTag(Element):

#     def render(self, )






