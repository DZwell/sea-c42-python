class Element(object):
    indent = '    '

    def __init__(self, tag, content, **kwargs):
        self.tag = tag
        self.content = ''
        self.childElements = []
        self.attributes = kwargs
        if content != '':
            self.append(content)

    def append(self, content):
        if isinstance(content, Element):
            self.childElements.append(content)
        else:
            self.content += content

    def render(self, file_out, indent = ""):
        # Render the open tag
        self.renderOpenTag(file_out, indent)
        file_out.write('\n')
        # Iterate through all child elements, rendering them recursively
        for child in self.childElements:
            child.render(file_out, indent + Element.indent)
        # Render string content
        if self.content != '':
            file_out.write(indent + Element.indent + self.content + '\n')
        # Render close tag
        self.renderCloseTag(file_out, indent)
        if indent != '':
            file_out.write('\n')

    def renderOpenTag(self, file_out, indent = "", selfClosing = False):
        file_out.write(indent + '<' + self.tag);
        for k, v in self.attributes.items():
            file_out.write(' ' + k + '="' + v + '"')
        if selfClosing:
            file_out.write(' />')
        else:
            file_out.write('>')

    def renderCloseTag(self, file_out, indent = ""):
        file_out.write(indent + '</' + self.tag + '>')


class Html(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, 'html', '', **kwargs)


class Body(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, 'body', '', **kwargs)


class Head(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, 'head', '', **kwargs)


class P(Element):

    def __init__(self, content, **kwargs):
        Element.__init__(self, 'p', content, **kwargs)


class OneLineTag(Element):

    def __init__(self, tag, content, **kwargs):
        Element.__init__(self, tag, content, **kwargs)

    def append(self, content):
        if not isinstance(content, str):
            raise Exception("OneLineTag content must be a string")
        Element.append(self, content)

    def render(self, file_out, indent = ""):
        Element.renderOpenTag(self, file_out, indent)
        file_out.write(self.content)
        Element.renderCloseTag(self, file_out, '')
        file_out.write('\n')


class Title(OneLineTag):

    def __init__(self, content, **kwargs):
        OneLineTag.__init__(self, 'Title', content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, tag, **kwargs):
        Element.__init__(self, tag, '', **kwargs)

    def append(self, content):
        raise Exception("Content cannot be set on a self closing tag element")

    def render(self, file_out, indent = ""):
        Element.renderOpenTag(self, file_out, indent, True)
        file_out.write('\n')


class Hr(SelfClosingTag):

    def __init__(self, **kwargs):
        SelfClosingTag.__init__(self, 'hr', **kwargs)


class Br(SelfClosingTag):

    def __init__(self, **kwargs):
        SelfClosingTag.__init__(self, 'br', **kwargs)


class A(OneLineTag):

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        OneLineTag.__init__(self, 'a', content, **kwargs)











