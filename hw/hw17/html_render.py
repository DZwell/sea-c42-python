# #!/usr/bin/env python


class Element(object):

    INDENT = '\t'

    def __init__(self, tag, content=None):
        self.tag = tag
        self.content = []
        self.append(content)


    def append(self, content):
        if(content):
            self.content.append(content)

    def render(self, f, indent = ""):
        f.write("%s<%s>\n" % (indent, self.tag))
        current_indent = indent + Element.INDENT
        for content in self.content:
            if isinstance(content, str):
                f.write("%s%s\n" % (current_indent, content))
            elif isinstance(content, Element):
                content.render(f, current_indent)

        f.write("%s</%s>\n" % (indent, self.tag))


class Body(Element):

    def __init__(self):
        Element.__init__(self, 'body', '')


class Html(Element):

    def __init__(self):
        Element.__init__(self, 'html', '')


class P(Element):

    def __init__(self, content):
        Element.__init__(self, 'p', content)









# class Element(object):

#     indent = '    '

#     def __init__(self, tag, content):
#         self.tag = tag
#         self.content = ''
#         self.childElements = []
#         self.append(content)

#     def append(self, content):
#         if isinstance(content, Element):
#             self.childElements.append(content)
#         else:
#             self.content += content

#     def render(self, file_out, indent = ""):
#         file_out.write(indent + '<' + self.tag + '>\n')
#         for child in self.childElements:
#             child.render(file_out, indent + Element.indent)
#         if(self.content != ''):
#             file_out.write(indent + Element.indent + self.content + '\n')
#         file_out.write(indent + '</' + self.tag + '>')
#         if(indent != ''):
#             file_out.write('\n')




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






