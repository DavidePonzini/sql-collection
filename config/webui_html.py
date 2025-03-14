import html
import sql_errors
import utils
from llm import MessageRole

CSS = utils.load_file('style.css')


class HtmlComponent:
    def __init__(self, html: str):
        self.html = html

    def __str__(self):
        return self.html


class Icon:
    USER = '''
        <div class="icon">
            <i class="fas fa-user"></i>
            <br>
            You 
        </div>
    '''
    ASSISTANT = '''
        <div class="icon">
            <i class="fas fa-robot"></i>
            <br>
            AI 
        </div>
    '''
    NO_ICON = ''

def exception_to_html(exception: sql_errors.SQLException) -> str:
    traceback = '\n' + '\n'.join(exception.traceback)
    traceback = html.escape(traceback)

    return f'''
        <b class="m">{exception}</b>
        <br>
        <pre class="code m">{traceback}</pre>
    '''

class Chat(HtmlComponent):
    def __init__(self, id: int):
        super().__init__(f'''
                <style>{CSS}</style>
            
                <div class="box" id="chat{id}"></div>
            ''')

class Message(HtmlComponent):
    def __init__(self, role: MessageRole, content: str, msg_id: int):
        super().__init__(f'''
                <div class="messagebox messagebox-{role}" id="msg{msg_id}">
                    {Icon.ASSISTANT if role == MessageRole.ASSISTANT else Icon.NO_ICON}    
                    <div class="message">
                        {content}
                    </div>
                    {Icon.USER if role == MessageRole.USER else Icon.NO_ICON}
                </div>
            ''')
