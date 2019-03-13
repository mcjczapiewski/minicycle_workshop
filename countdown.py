
import curses
import time
from datetime import datetime, timedelta

DELAY = 0.1

SCHEDULE = [
    (' 9:20', ' 9:25', 'Introduction'),
    (' 9:25', ' 9:35', 'Prepare teams and code'),
    (' 9:35', '10:00', 'Initial planning'),
    '',
    ('10:00', '10:50', 'Iteration 1'),
    ('10:50', '11:00', 'Review and retro'),
    '',
    ('11:00', '11:50', 'Iteration 2'),
    ('11:50', '12:00', 'Review and retro'),
    '',
    ('12:00', '13:00', '-- Lunch break --'),
    '',
    ('13:00', '13:50', 'Iteration 3'),
    ('13:50', '14:00', 'Review and retro'),
    '',
    ('14:00', '14:50', 'Iteration 4'),
    ('14:50', '15:00', 'Review and retro'),
    '',
    ('15:00', '15:10', 'Closing'),
]


def draw(stdscr, now):
    height, width = stdscr.getmaxyx()
    start_y = height // 2 - len(SCHEDULE) // 2
    start_x = 10

    stdscr.clear()
    for i, element in enumerate(SCHEDULE):
        if isinstance(element, str):
            attr = curses.color_pair(curses.COLOR_WHITE)
            stdscr.addstr(start_y + i, start_x, element, attr)
        else:
            t_start_str, t_end_str, title = element
            t_start = parse_datetime(t_start_str)
            t_end = parse_datetime(t_end_str)
            desc = f'{t_start_str} -- {t_end_str}  {title}'

            if t_end <= now:
                attr = curses.color_pair(curses.COLOR_GREEN)
            elif t_start <= now < t_end:
                attr = curses.color_pair(curses.COLOR_WHITE) | curses.A_BOLD
            else:
                attr = curses.color_pair(curses.COLOR_WHITE) | curses.A_DIM

            stdscr.addstr(start_y + i, start_x, desc, attr)

            if t_start <= now < t_end:
                dt = t_end - now
                hours = dt.seconds // 3600
                minutes = (dt.seconds // 60) % 60
                seconds = dt.seconds % 60
                if hours:
                    countdown = f'{hours:01}:{minutes:02}:{seconds:02}'
                else:
                    countdown = f'  {minutes:02}:{seconds:02}'
                stdscr.addstr(start_y + i, start_x + 40, countdown, attr)

    stdscr.refresh()


def parse_datetime(s):
    h, m = s.split(':')
    return datetime.now().replace(hour=int(h), minute=int(m),
                                  second=0, microsecond=0)


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1)
    try:
        while True:
            now = datetime.now()
            draw(stdscr, now)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    curses.wrapper(main)
