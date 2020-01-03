import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1400,600))
pygame.display.set_caption('Font test')

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)
BLACK  = (0,0,0)

fonts = pygame.font.get_fonts()
objs = []
srfcs = []
rects = []

to_del = (
    "gadugi",
    "holomdlassets",
    "inkfree",
    "javanesetext",
    "leelawadeeui",
    "leelawadeeuisemilight",
    "malgungothic",
    "malgungothicsemilight",
    "microsofthimalaya",
    "microsoftjhengheimicrosoftjhengheiui",
    "microsoftjhengheimicrosoftjhengheiuibold",
    "microsoftjhengheimicrosoftjhengheiuilight",
    "microsoftnewtailue",
    "microsofttaile",
    "microsoftyibaiti",
    "mingliuextbpmingliuextbmingliuhkscsextb",
    "mongolianbaiti",
    "mvboli",
    "myanmartext",
    "nirmalaui",
    "nirmalauisemilight",
    "segoemdlassets",
    "segoeuisymbol",
    "simsunnsimsun",
    "simsunextb",
    "symbol",
    "webdings",
    "wingdings",
    "agencyfb",
    "algerian",
    "arialrounded",
    "baskervilleoldface",
    "bauhaus",
    "bell",
    "berlinsansfb",
    "berlinsansfbdemi",
    "bernardcondensed",
    "blackadderitc",
    "bodoni",
    "bodoniblack",
    "bodonicondensed",
    "bodonipostercompressed",
    "bookshelfsymbol",
    "bradleyhanditc",
    "britannic",
    "broadway",
    "brushscript",
    "californianfb",
    "calisto",
    "castellar",
    "centaur",
    "chiller",
    "colonna",
    "cooperblack",
    "copperplategothic",
    "curlz",
    "edwardianscriptitc",
    "elephant",
    "engravers",
    "erasitc",
    "erasdemiitc",
    "erasmediumitc",
    "felixtitling",
    "footlight",
    "forte",
    "freestylescript",
    "frenchscript",
    "gigi",
    "gloucesterextracondensed",
    "goudyoldstyle",
    "goudystout",
    "harlowsolid",
    "harrington",
    "hightowertext",
    "imprintshadow",
    "informalroman",
    "jokerman",
    "juiceitc",
    "kristenitc",
    "kunstlerscript",
    "lucidabright",
    "lucidacalligraphy",
    "lucidafax",
    "lucidafaxregular",
    "lucidahandwriting",
    "lucidasansroman",
    "lucidasansregular",
    "lucidasanstypewriter",
    "lucidasanstypewriteroblique",
    "lucidasanstypewriterregular",
    "magneto",
    "maiandragd",
    "maturascriptcapitals",
    "modernno",
    "msoutlook",
    "msreferencespecialty",
    "extra",
    "niagaraengraved",
    "niagarasolid",
    "ocraextended",
    "oldenglishtext",
    "onyx",
    "palacescript",
    "papyrus",
    "parchment",
    "perpetua",
    "perpetuatitling",
    "playbill",
    "poorrichard",
    "pristina",
    "rage",
    "ravie",
    "rockwell",
    "rockwellcondensed",
    "holomdl2assets",
    "segoemdl2assets",
    "bookshelfsymbol7",
    "bauhaus93",
    "segoeuiemoji",
    "segoeuihistoric",
    "modernno20",
    "rockwellextra",
    "script",
    "showcardgothic",
    "snapitc",
    "stencil",
    "tempussansitc",
    "vinerhanditc",
    "vivaldi",
    "vladimirscript",
    "widelatin",
    "wingdings2",
    "wingdings3"
)

for delete in to_del:
    if delete in fonts:
        fonts.remove(delete)
    else:
        print(delete)

for index, i in enumerate(fonts):
    objs.append(pygame.font.SysFont(i, 36))
    srfcs.append(objs[-1].render(str(index) + 'Ľúbim svet', True, BLACK))
    rect = srfcs[-1].get_rect()
    x = 0
    if index < 15:
        x = 100
        y = index*36 + 36
    elif index < 30:
        x = 380
        y = (30-index)*36
    elif index < 45:
        x = 700
        y = (45-index)*36
    elif index < 60:
        x = 950
        y = (60-index)*36
    elif index <= 75:
        x = 1200
        y = (75-index)*32+32

    rect.center = (x, y)
    rects.append(rect)

while True:
    screen.fill(WHITE)
    for index in range(len(rects)):
        screen.blit(srfcs[index], rects[index])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
