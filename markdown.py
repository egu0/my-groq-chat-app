import time
from wcwidth import wcswidth
import shutil
from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import Terminal256Formatter

line_buffer = ''
thinking = None


def get_thinking():
    return thinking


def set_thinking(value):
    global thinking
    thinking = value


def append_file(s: str):
    with open('logs/temp.txt', 'a', encoding='utf-8') as file:
        file.write(s + '\n')


def hit_row_limit():
    width = screen_columns()
    # 如果行缓冲区的长度大于等于当前终端的列数的 90%，返回 True
    return wcswidth(line_buffer) >= width * 0.9


def screen_columns():
    return shutil.get_terminal_size().columns


def end_current_line():
    global line_buffer
    line_buffer = ''
    print()


class Colors:
    RESET = "\033[0m"  # 重置颜色
    GREY = "\033[90m"  # 灰色


def do_output(cur_token: str):
    global line_buffer
    if get_thinking():
        print(f"\r{Colors.GREY}{line_buffer}{Colors.RESET}", end="")
    else:
        highlighted_text = highlight(
            line_buffer, MarkdownLexer(), Terminal256Formatter(style='solarized-light'))
        # print(repr(highlighted_text[:-1]))
        print('\r' + highlighted_text[:-1], end="")
    #  如果当前 token 包含 '</think>'，则将 thinking 置为 False
    if '</think>' in cur_token:
        set_thinking(False)


def render_single_line(token: str):
    if token is None:
        return

    if '\n\n' == token:
        end_current_line()
        end_current_line()
        return
    elif '\n' == token:
        end_current_line()
        return

    global line_buffer
    items = token.split('\n')
    if len(items) == 1:
        line_buffer += items[0]
        do_output(token)
        if hit_row_limit():
            end_current_line()
        return

    for item in items:
        if item == '':
            end_current_line()
        else:
            line_buffer += item
            do_output(token)
            if hit_row_limit():
                end_current_line()


tokens = ['',
          '<think>',
          '\n',
          'Okay',
          ',',
          ' so',
          ' I',
          "'m",
          ' trying',
          ' to',
          ' figure',
          ' out',
          ' how',
          ' to',
          ' respond',
          ' to',
          ' this',
          ' user',
          "'s",
          ' query',
          '.',
          ' They',
          ' want',
          ' me',
          ' to',
          ' generate',
          ' a',
          ' response',
          ' that',
          ' includes',
          ' a',
          ' list',
          ',',
          ' a',
          ' link',
          ',',
          ' titles',
          ',',
          ' and',
          ' so',
          ' on',
          '.',
          ' Let',
          ' me',
          ' break',
          ' this',
          ' down',
          '.\n\n',
          'First',
          ',',
          ' I',
          ' need',
          ' to',
          ' understand',
          ' the',
          ' context',
          '.',
          ' The',
          ' user',
          ' provided',
          ' an',
          ' example',
          ' response',
          ' that',
          ' includes',
          ' a',
          ' title',
          ',',
          ' a',
          ' numbered',
          ' list',
          ' with',
          ' links',
          ',',
          ' and',
          ' some',
          ' additional',
          ' information',
          '.',
          ' They',
          ' also',
          ' mentioned',
          ' that',
          ' the',
          ' response',
          ' should',
          ' be',
          ' helpful',
          ' and',
          ' engaging',
          ',',
          ' using',
          ' proper',
          ' formatting',
          '.\n\n',
          'I',
          ' should',
          ' start',
          ' by',
          ' identifying',
          ' the',
          ' main',
          ' topic',
          '.',
          ' The',
          ' example',
          ' given',
          ' is',
          ' about',
          ' "',
          'Top',
          ' ',
          '5',
          ' Product',
          'ivity',
          ' Tools',
          ' for',
          ' Remote',
          ' Work',
          '."',
          ' That',
          ' seems',
          ' like',
          ' a',
          ' popular',
          ' topic',
          ',',
          ' so',
          ' it',
          "'s",
          ' a',
          ' good',
          ' choice',
          '.',
          ' Now',
          ',',
          ' I',
          ' need',
          ' to',
          ' come',
          ' up',
          ' with',
          ' a',
          ' similar',
          ' structure',
          ' but',
          ' perhaps',
          ' on',
          ' a',
          ' different',
          ' topic',
          ' to',
          ' show',
          ' variety',
          '.\n\n',
          'Wait',
          ',',
          ' maybe',
          ' I',
          ' should',
          ' stick',
          ' to',
          ' the',
          ' same',
          ' topic',
          ' to',
          ' align',
          ' with',
          ' the',
          ' user',
          "'s",
          ' example',
          '.',
          ' That',
          ' way',
          ',',
          ' the',
          ' response',
          ' will',
          ' be',
          ' consistent',
          ' with',
          ' what',
          ' they',
          ' provided',
          '.',
          ' So',
          ',',
          ' I',
          "'ll",
          ' go',
          ' with',
          ' productivity',
          ' tools',
          ' for',
          ' remote',
          ' work',
          '.\n\n',
          'Next',
          ',',
          ' I',
          ' need',
          ' to',
          ' create',
          ' a',
          ' list',
          ' of',
          ' tools',
          '.',
          ' The',
          ' example',
          ' had',
          ' five',
          ' tools',
          ',',
          ' each',
          ' with',
          ' a',
          ' brief',
          ' description',
          ' and',
          ' a',
          ' link',
          '.',
          ' I',
          ' should',
          ' make',
          ' sure',
          ' each',
          ' item',
          ' is',
          ' clear',
          ' and',
          ' the',
          ' links',
          ' are',
          ' real',
          '.',
          ' Let',
          ' me',
          ' think',
          ' of',
          ' five',
          ' popular',
          ' productivity',
          ' tools',
          ':',
          ' T',
          'rello',
          ',',
          ' Slack',
          ',',
          ' Google',
          ' Drive',
          ',',
          ' Zoom',
          ',',
          ' and',
          ' Microsoft',
          ' Teams',
          '.',
          ' These',
          ' are',
          ' all',
          ' well',
          '-known',
          ' and',
          ' widely',
          ' used',
          '.\n\n',
          'Now',
          ',',
          ' I',
          "'ll",
          ' write',
          ' a',
          ' short',
          ' description',
          ' for',
          ' each',
          '.',
          ' For',
          ' example',
          ',',
          ' T',
          'rello',
          ' is',
          ' great',
          ' for',
          ' task',
          ' management',
          ',',
          ' Slack',
          ' for',
          ' communication',
          ',',
          ' Google',
          ' Drive',
          ' for',
          ' storage',
          ',',
          ' Zoom',
          ' for',
          ' meetings',
          ',',
          ' and',
          ' Microsoft',
          ' Teams',
          ' for',
          ' collaboration',
          '.',
          ' I',
          "'ll",
          ' include',
          ' the',
          ' official',
          ' links',
          ' for',
          ' each',
          ' to',
          ' make',
          ' it',
          ' helpful',
          '.\n\n',
          'After',
          ' the',
          ' list',
          ',',
          ' I',
          "'ll",
          ' add',
          ' a',
          ' section',
          ' on',
          ' additional',
          ' tips',
          ' for',
          ' remote',
          ' work',
          '.',
          ' The',
          ' example',
          ' had',
          ' three',
          ' tips',
          ':',
          ' creating',
          ' a',
          ' dedicated',
          ' workspace',
          ',',
          ' establishing',
          ' a',
          ' routine',
          ',',
          ' and',
          ' regular',
          ' communication',
          '.',
          ' I',
          ' can',
          ' follow',
          ' that',
          ' structure',
          '.',
          ' Maybe',
          ' I',
          ' can',
          ' add',
          ' a',
          ' tip',
          ' about',
          ' time',
          ' management',
          ' tools',
          ' or',
          ' using',
          ' a',
          ' VPN',
          ' for',
          ' security',
          ',',
          ' but',
          ' the',
          ' example',
          ' had',
          ' three',
          ',',
          ' so',
          ' I',
          "'ll",
          ' stick',
          ' to',
          ' that',
          '.\n\n',
          'I',
          ' should',
          ' also',
          ' include',
          ' a',
          ' final',
          ' recommendation',
          ',',
          ' like',
          ' suggesting',
          ' the',
          ' user',
          ' try',
          ' a',
          ' couple',
          ' of',
          ' these',
          ' tools',
          ' and',
          ' see',
          ' what',
          ' works',
          ' best',
          ' for',
          ' them',
          '.',
          ' That',
          ' makes',
          ' the',
          ' response',
          ' more',
          ' personalized',
          ' and',
          ' helpful',
          '.\n\n',
          'I',
          ' need',
          ' to',
          ' make',
          ' sure',
          ' the',
          ' formatting',
          ' is',
          ' clean',
          '.',
          ' Using',
          ' headers',
          ' with',
          ' ###',
          ',',
          ' bullet',
          ' points',
          ' with',
          ' numbers',
          ',',
          ' and',
          ' links',
          ' in',
          ' brackets',
          '.',
          ' I',
          "'ll",
          ' avoid',
          ' any',
          ' markdown',
          ' since',
          ' the',
          ' user',
          ' mentioned',
          ' not',
          ' to',
          ' use',
          ' any',
          ',',
          ' but',
          ' in',
          ' the',
          ' example',
          ',',
          ' they',
          ' used',
          ' markdown',
          '.',
          ' Wait',
          ',',
          ' the',
          ' user',
          ' said',
          ' to',
          ' include',
          ' links',
          ' and',
          ' titles',
          ',',
          ' so',
          ' maybe',
          ' using',
          ' headers',
          ' is',
          ' okay',
          '.',
          ' I',
          "'ll",
          ' follow',
          ' the',
          ' example',
          "'s",
          ' structure',
          '.\n\n',
          'Let',
          ' me',
          ' double',
          '-check',
          ' the',
          ' links',
          ' to',
          ' ensure',
          ' they',
          "'re",
          ' correct',
          '.',
          ' T',
          'rello',
          '.com',
          ',',
          ' Slack',
          '.com',
          ',',
          ' Google',
          '.com',
          '/dr',
          'ive',
          ',',
          ' Zoom',
          '.us',
          ',',
          ' and',
          ' Microsoft',
          '.com',
          '/',
          'teams',
          '.',
          ' All',
          ' correct',
          '.\n\n',
          'I',
          ' should',
          ' also',
          ' keep',
          ' the',
          ' language',
          ' clear',
          ' and',
          ' concise',
          ',',
          ' avoiding',
          ' any',
          ' j',
          'argon',
          '.',
          ' The',
          ' goal',
          ' is',
          ' to',
          ' be',
          ' helpful',
          ' and',
          ' informative',
          ' without',
          ' overwhelming',
          ' the',
          ' reader',
          '.\n\n',
          'Finally',
          ',',
          ' I',
          "'ll",
          ' review',
          ' the',
          ' entire',
          ' response',
          ' to',
          ' make',
          ' sure',
          ' it',
          ' flows',
          ' well',
          ' and',
          ' covers',
          ' all',
          ' the',
          ' points',
          ' the',
          ' user',
          ' requested',
          ':',
          ' a',
          ' title',
          ',',
          ' a',
          ' numbered',
          ' list',
          ' with',
          ' links',
          ',',
          ' additional',
          ' tips',
          ',',
          ' and',
          ' a',
          ' closing',
          ' statement',
          '.\n\n',
          'I',
          ' think',
          ' that',
          "'s",
          ' it',
          '.',
          ' Time',
          ' to',
          ' put',
          ' it',
          ' all',
          ' together',
          ' in',
          ' the',
          ' response',
          '.\n',
          '</think>',
          '\n\n',
          '###',
          ' Top',
          ' ',
          '5',
          ' Product',
          'ivity',
          ' Tools',
          ' for',
          ' Remote',
          ' Work',
          '\n\n',
          'St',
          'aying',
          ' productive',
          ' while',
          ' working',
          ' remotely',
          ' can',
          ' be',
          ' challenging',
          ',',
          ' but',
          ' the',
          ' right',
          ' tools',
          ' can',
          ' make',
          ' a',
          ' significant',
          ' difference',
          '.',
          ' Here',
          ' are',
          ' five',
          ' essential',
          ' tools',
          ' to',
          ' enhance',
          ' your',
          ' remote',
          ' work',
          ' experience',
          ':\n\n',
          '1',
          '.',
          ' **',
          'T',
          'rello',
          '**',
          ' -',
          ' A',
          ' versatile',
          ' project',
          ' management',
          ' tool',
          ' that',
          ' uses',
          ' boards',
          ',',
          ' lists',
          ',',
          ' and',
          ' cards',
          ' to',
          ' organize',
          ' tasks',
          '.',
          '  \n',
          '  ',
          ' [',
          'T',
          'rello',
          '](',
          'https',
          '://',
          't',
          'rello',
          '.com',
          ')\n\n',
          '2',
          '.',
          ' **',
          'Sl',
          'ack',
          '**',
          ' -',
          ' A',
          ' communication',
          ' platform',
          ' designed',
          ' for',
          ' team',
          ' collaboration',
          ',',
          ' offering',
          ' real',
          '-time',
          ' messaging',
          ',',
          ' video',
          ' calls',
          ',',
          ' and',
          ' file',
          ' sharing',
          '.',
          '  \n',
          '  ',
          ' [',
          'Sl',
          'ack',
          '](',
          'https',
          '://',
          'slack',
          '.com',
          ')\n\n',
          '3',
          '.',
          ' **',
          'Google',
          ' Drive',
          '**',
          ' -',
          ' A',
          ' cloud',
          ' storage',
          ' service',
          ' where',
          ' you',
          ' can',
          ' store',
          ' and',
          ' share',
          ' files',
          ',',
          ' collaborate',
          ' on',
          ' documents',
          ',',
          ' and',
          ' access',
          ' your',
          ' data',
          ' from',
          ' anywhere',
          '.',
          '  \n',
          '  ',
          ' [',
          'Google',
          ' Drive',
          '](',
          'https',
          '://',
          'www',
          '.google',
          '.com',
          '/dr',
          'ive',
          '/',
          ')\n\n',
          '4',
          '.',
          ' **',
          'Zoom',
          '**',
          ' -',
          ' A',
          ' video',
          ' confer',
          'encing',
          ' tool',
          ' perfect',
          ' for',
          ' virtual',
          ' meetings',
          ',',
          ' web',
          'inars',
          ',',
          ' and',
          ' remote',
          ' team',
          ' discussions',
          '.',
          '  \n',
          '  ',
          ' [',
          'Zoom',
          '](',
          'https',
          '://',
          'zoom',
          '.us',
          ')\n\n',
          '5',
          '.',
          ' **',
          'Microsoft',
          ' Teams',
          '**',
          ' -',
          ' An',
          ' all',
          '-in',
          '-one',
          ' collaboration',
          ' platform',
          ' that',
          ' integrates',
          ' chat',
          ',',
          ' video',
          ' meetings',
          ',',
          ' and',
          ' document',
          ' sharing',
          '.',
          '  \n',
          '  ',
          ' [',
          'Microsoft',
          ' Teams',
          '](',
          'https',
          '://',
          'www',
          '.microsoft',
          '.com',
          '/en',
          '-us',
          '/m',
          'icrosoft',
          '-',
          'teams',
          ')\n\n',
          '###',
          ' Additional',
          ' Tips',
          ' for',
          ' Remote',
          ' Work',
          ' Success',
          '\n\n',
          '-',
          ' **',
          'Create',
          ' a',
          ' Dedicated',
          ' Workspace',
          '**:',
          ' Design',
          'ate',
          ' a',
          ' specific',
          ' area',
          ' for',
          ' work',
          ' to',
          ' maintain',
          ' a',
          ' healthy',
          ' work',
          '-life',
          ' balance',
          '.\n',
          '-',
          ' **',
          'Establish',
          ' a',
          ' Routine',
          '**:',
          ' Set',
          ' clear',
          ' working',
          ' hours',
          ' and',
          ' stick',
          ' to',
          ' them',
          ' to',
          ' stay',
          ' focused',
          ' and',
          ' productive',
          '.\n',
          '-',
          ' **',
          'Communic',
          'ate',
          ' Regular',
          'ly',
          '**:',
          ' Use',
          ' the',
          ' tools',
          ' above',
          ' to',
          ' keep',
          ' in',
          ' touch',
          ' with',
          ' your',
          ' team',
          ' and',
          ' avoid',
          ' feelings',
          ' of',
          ' isolation',
          '.\n\n',
          'By',
          ' incorporating',
          ' these',
          ' tools',
          ' and',
          ' tips',
          ' into',
          ' your',
          ' remote',
          ' work',
          ' setup',
          ',',
          ' you',
          ' can',
          ' stay',
          ' efficient',
          ' and',
          ' connected',
          '.',
          ' Try',
          ' them',
          ' out',
          ' and',
          ' see',
          ' what',
          ' works',
          ' best',
          ' for',
          ' you',
          '!',
          '',
          ]

if __name__ == "__main__":
    set_thinking(True)
    for tk in tokens:
        render_single_line(tk)
        time.sleep(0.05)
