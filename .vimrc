set nocompatible              " be iMproved, required
filetype off                  " required
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin),
"Plugin 'file:///home/jjeaby/Dev/tools/vim-plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}
" All of your Plugins must be added before the following line
Plugin 'tpope/vim-surround'
Plugin 'uarun/vim-protobuf'
Plugin 'taq/vim-git-branch-info'
Plugin 'bling/vim-airline'
Plugin 'tomtom/tlib_vim'
Plugin 'majutsushi/tagbar'
Plugin 'gre/play2vim.git'
Plugin 'othree/html5.vim'
Plugin 'rodjek/vim-puppet'
Plugin 'scrooloose/nerdcommenter'
Plugin 'vim-scripts/L9'
Plugin 'wikitopian/hardmode'
Plugin 'vim-scripts/Align'
Plugin 'rking/ag.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'luochen1990/rainbow'
Plugin 'jtai/vim-womprat'
Plugin 'chrisbra/vim-diff-enhanced'
Plugin 'derekwyatt/vim-sbt'
Plugin 'elzr/vim-json'
Plugin 'noahfrederick/vim-hemisu'
Plugin 'mkitt/tabline.vim'
Plugin 'junegunn/vim-easy-align'
"Plugin 'Shougo/neocomplcache.vim'
Plugin 'kennethzfeng/vim-raml'
Plugin 'editorconfig/editorconfig-vim'
Plugin 'grassdog/tagman.vim'
" Colorscheme plugins
Plugin 'endel/vim-github-colorscheme'
Plugin 'flazz/vim-colorschemes'
Plugin 'vim-scripts/ScrollColors'
Plugin 'nanotech/jellybeans.vim'
Plugin 'junegunn/seoul256.vim'
Plugin 'reedes/vim-colors-pencil'
Plugin 'zenorocha/dracula-theme', {'rtp': 'vim/'}
Plugin 'mtglsk/mushroom'
Plugin 'aradunovic/perun.vim'
Plugin 'ayu-theme/ayu-vim'
Plugin 'morhetz/gruvbox'
" python
Plugin 'hdima/python-syntax'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'sonph/onehalf', {'rtp': 'vim/'}
call vundle#end()            " required
"filetype plugin indent on    " required
""""""""""""""""""""""""""""""""""
" VIM General settings
""""""""""""""""""""""""""""""""""
" On even hour, use dark colortheme
" On odd hour, use light colortheme
set t_Co=256          " enables 256 colors
set termguicolors     " enable true colors support
syntax enable
set encoding=utf-8
"let ayucolor="light"  " for light version of theme
"let ayucolor="mirage" " for mirage version of theme
"let ayucolor="dark"   " for dark version of theme
"colorscheme ayu
set background=dark
"let g:seoul256_background = 233
"colo seoul256
let g:solarized_termcolors=256
colo gruvbox
" vim reads the file when it changes
" check one time after 4s of inactivity in normal mode
set autoread
au CursorHold * checktim
set noundofile
set mouse=a
set switchbuf=useopen " reveal already opened files from the
                      " quickfix window instead of opening new
                      " buffers
set history=1000      " remember more commands and search history
set undolevels=1000   " use many muchos levels of undo
set hidden            " hide buffers instead of closing them this
                      " means that the current buffer can be put
                      " to background without being written; and
                      " that marks and undo history are preserved
set nobackup          " do not keep backup files, it's 70's style cluttering
set noswapfile        " do not write annoying intermediate swap files,
set showcmd           " show the command being typed
set ruler             " Always show current positions along the bottom
set nostartofline     " leave my cursor where it was
set colorcolumn=120   " highlight maximum line length
set cursorline        " highlight current line
set number
set numberwidth=5     " We are good up to 99999 lines
set backspace=2       " make backspace work like most other apps
let g:jsx_ext_required    = 0 "If you would like JSX in .js files
let delimitMate_expand_cr = 1
" Vim file tree setting
" d creates a new directory
" % creates and opens a new file
" D deletes a directory or file
" R renames a file
" o opens the file in a horizontal split
" v opens the file in a vertical split
let g:netrw_liststyle=3
let g:netrw_winsize = 1
" Neocompletecache setting
"let g:neocomplcache_enable_at_startup = 1
""""""""""""""""""""""""""""""""""
" Hide tool bar for macvim
""""""""""""""""""""""""""""""""""
if has("gui_running")
    set guioptions=egmrt
endif
""""""""""""""""""""""""""""""""""
" Switch on filetype detection and loads
" indent file (indent.vim) for specific file types
""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""
"set font
""""""""""""""""""""""""""""""""""
set gfn=D2Coding:h15
""""""""""""""""""""""""""""""""""
" set nu " Number lines
""""""""""""""""""""""""""""""""""
set hls " highlight search
set lbr " linebreak
""""""""""""""""""""""""""""""""""
" Use 2 space instead of tab during format
""""""""""""""""""""""""""""""""""
"set tabstop=2     " determines how many space tap should be counted for when tab is read
"set shiftwidth=2
"set softtabstop=2 " determines how many space tap should be countered for when tab key is hit
"set expandtab
"set autoindent    " Copy indent from the row above
"set smartindent
"set cindent
""""""""""""""""""""""""""""""""""""""""""""
""""""""""""For python""""""""""""""""""""""
filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
set softtabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab
""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""
" For Python
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set expandtab |
    "\ set autoindent |
    \ set fileformat=unix
let python_highlight_all = 1
" Indent guide plugin setting (https://github.com/nathanaelkane/vim-indent-guides)
let g:indent_guides_auto_colors = 0
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  guibg=red   ctermbg=3
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven guibg=green ctermbg=4
" For XML
au BufNewFile,BufRead *.xml
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix
""""""""""""""""""""""""""""""""""
" NERD Tree
""""""""""""""""""""""""""""""""""
nmap ne :NERDTreeToggle<CR>
" Show hidden files, too
let NERDTreeShowFiles=1
let NERDTreeShowHidden=1
" Highlight the selected entry in the tree
let NERDTreeHighlightCursorline=1
""""""""""""""""""""""""""""""""""
" GIT set-ups
""""""""""""""""""""""""""""""""""
set laststatus=2                          " Enables the status line at the bottom of Vim
set statusline=%{GitBranchInfoString()}\ \ \ \ \ %f
let g:git_branch_status_head_current=1    " Display only the current branch
""""""""""""""""""""""""""""""""""
" CTags
""""""""""""""""""""""""""""""""""
set tags=./tags;/
""""""""""""""""""""""""""""""""""
" Search Highlights
""""""""""""""""""""""""""""""""""
set hlsearch            " turn off highlight searches, but:
                        " Turn hlsearch off/on with CTRL-N
:map <silent> <C-N> :se invhlsearch<CR>
""""""""""""""""""""""""""""""""""
" Key Maps
""""""""""""""""""""""""""""""""""
set pastetoggle=<F1>                          " retain original indents when pating
map <F2> :TagbarToggle<CR>                    " Tagbar Toggle
""""""""""""""""""""""""""""""""""
" Rainbow Parentheses
""""""""""""""""""""""""""""""""""
let g:rainbow_active = 1
let g:rainbow_conf   = {
\   'ctermfgs': ['darkblue', 'darkgreen', 'darkcyan', 'darkmagenta']
\}
"""""""""""""""""""""""""""""""""""""""""
" copy to OS clipboard
"""""""""""""""""""""""""""""""""""""""""
" Set clipboard t0 unnamedplus only if it's not Mac OS X
set clipboard=unnamed
if has("unix")
  let s:uname = system("uname")
  if s:uname == "Linux\n"
    set clipboard=unnamedplus
  endif
else
    set clipboard=unnamed
endif
vnoremap <C-c> "*y
vnoremap <C-p> "*p
vmap ,c "+y
vmap ,p "*p
set wildignore+=*/tmp/*,*/target/*,*.so,*.swp,*.zip,*.tag
""""""""""""""""""""""""""""""""""
" Neocomplcache
""""""""""""""""""""""""""""""""""
"let g:neocomplcache_enable_at_startup = 1
""""""""""""""""""""""""""""""""""
" vim-airline
""""""""""""""""""""""""""""""""""
"let g:airline_theme='onehalfdark'
let g:airline_theme = 'gruvbox'
function! AccentDemo()
  let keys = ['춤','추','는','망','고']
  for k in keys
    call airline#parts#define_text(k, k)
  endfor
  call airline#parts#define_accent('춤', 'red')
  call airline#parts#define_accent('추', 'red')
  call airline#parts#define_accent('는', 'red')
  call airline#parts#define_accent('망', 'red')
  call airline#parts#define_accent('고', 'red')
  let g:airline_section_a = airline#section#create(keys)
endfunction
autocmd VimEnter * call AccentDemo()
let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '>>>'
let g:airline#extensions#default#layout = [
\ [ 'a', 'b', 'c'],
\ [ 'z']
\ ]
""""""""""""""""""""""""""""""""""
" Disable arrow keys
""""""""""""""""""""""""""""""""""
" noremap <Up> <NOP>
" noremap <Down> <NOP>
" noremap <Left> <NOP>
" noremap <Right> <NOP>
""""""""""""""""""""""""""""""""""
" Folding Option
""""""""""""""""""""""""""""""""""
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za
" SimpleyFold plugin for python fold. Display docstirng when folded
let g:SimpylFold_docstring_preview = 1
set clipboard=unnamed           "yank, paste to system clipboard
""""""""""""""""""""""""""""""""""
"Easy Align
""""""""""""""""""""""""""""""""""
" Start interactive EasyAlign in visual mode (e.g. vipga)
xmap ga <Plug>(EasyAlign)

" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)

nnoremap <C-\> :vert winc ]<CR>

set hlsearch!

nnoremap <F4> :set hlsearch!<CR>
nmap <F8> :TagbarToggle<CR>

" 구문 강조 사용
if has("syntax")
 syntax on
endif
