" ordinary neovim
" plugins
" let need_to_install_plugins = 0
" if empty(glob('~/.vim/autoload/plug.vim'))
"     silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
"         \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
"     let need_to_install_plugins = 1
" endif

" Specify a directory for plugins
call plug#begin()

" Git
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-fugitive'
Plug 'Xuyuanp/nerdtree-git-plugin'

" Vim Themes
Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'ryanoasis/vim-devicons'

" For Python => :CocInstall coc-python
Plug 'davidhalter/jedi-vim', "{'do' : 'pip install jedi'}
Plug 'zchee/deoplete-jedi'

" For JavaScript
Plug 'pangloss/vim-javascript'

" For TypeScript
Plug 'HerringtonDarkholme/yats.vim' " TS Syntax

" For GraphQL
Plug 'jparise/vim-graphql'

" For Flutter, Dart => :CocInstall coc-flutter
Plug 'dart-lang/dart-vim-plugin'

" Utility for Vim
Plug 'neoclide/coc.nvim', {'branch': 'release'} " about coc
Plug 'preservim/nerdtree' " about directory tree
Plug 'jiangmiao/auto-pairs' " about auto pair
Plug 'scrooloose/nerdcommenter' " about comment
Plug 'terryma/vim-multiple-cursors' " about multiple line edit
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'ctrlpvim/ctrlp.vim' " fuzzy find files
Plug 'Lokaltog/vim-easymotion'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Check Codes
Plug 'neomake/neomake'
Plug 'scrooloose/syntastic'

Plug 'prettier/vim-prettier', { 'do': 'yarn install' }
Plug 'christoomey/vim-tmux-navigator' " allows cursor move between buffers

" Markdown Preview
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app & yarn install'  }

" Float terminal
Plug 'voldikss/vim-floaterm'

" Easy align
Plug 'junegunn/vim-easy-align'

Plug 'Chiel92/vim-autoformat'

" Plug 'tpope/vim-sensible'
" Plug 'itchyny/lightline.vim'
" Plug 'joshdick/onedark.vim'
" Plug 'ap/vim-buftabline'
" Plug 'jistr/vim-nerdtree-tabs'
" Plug 'dense-analysis/ale'
" Plug 'majutsushi/tagbar'
" Plug 'vim-scripts/indentpython.vim'
" Plug 'lepture/vim-jinja'
" Plug 'alvan/vim-closetag'
" Plug 'maxmellon/vim-jsx-pretty'

" Initialize plugin system
call plug#end()

" Set Autoformat only for python
au BufWrite *.py :Autoformat
au BufWrite *.cpp :Autoformat
au BufWrite *.dart :Autoformat

let g:autoformat_verbosemode=1
" OR:
let verbose=1

" Escape => kj
inoremap kj <Esc>

" Open/Hide float terminal => Alt + t
map <A-t> :FloatermToggle<cr>
tnoremap <A-t> <C-\><C-n>:FloatermHide!<cr>

" Open terminal in window => Alt + T
map <A-T> :term<cr>

" Control Floterm => Alt + -_=+
nnoremap <silent> <A--> :FloatermPrev<cr>
nnoremap <silent> <A-_> :FloatermNext<cr>
nnoremap <silent> <A-=> :FloatermNew<cr>
nnoremap <silent> <A-+> :FloatermKill<cr>

" Visual mode in float terminal => Alt + w
tnoremap <A-w> <C-\><C-n>

" Open file list => Alt + e
map <A-e> :GFiles<cr>

" Open buffer list => Alt + r
map <A-r> :Buffers<cr>

" Open commit list => Alt + c
map <A-c> :Commits<cr>

" Open commit list related to current buffer file => Alt + b
map <A-b> :BCommits<cr>

" Markdown Preview => Alt + m, Alt + Shift + m
map <A-m> :MarkdownPreview<cr>
map <A-S-m> :MarkdownPreviewStop<cr>

" Open finder => Alt + f
map <A-f> :Ag<cr>

" Open files => Alt + f
map <A-S-f> :Files<cr>

" Open finder => Alt + g
map <A-g> :Rg<cr>

" Move between windows => Ctrl + h, j, k, l

" Select word => Alt + v
" map <silent> <A-v> <Plug>(coc-range-select)

" Create window => Alt + d, Alt + Shift + d
map <A-d> :wincmd v<cr>
map <A-S-d> :wincmd s<cr>

" Move window to end => Alt + h, j, k, l
map <A-h> :wincmd H<cr>
map <A-j> :wincmd J<cr>
map <A-k> :wincmd K<cr>
map <A-l> :wincmd L<cr>

" Save & Quit => Alt + Enter
map <A-CR> :wq<cr>

" Quit => Alt + w
map <A-w> :q<cr>

" Quit force => Alt + q
map <A-q> :q!<cr>

" Save => Enter
map <CR> :w<cr>

" NERD Tree Toggle => .
map <silent> . :NERDTreeToggle<CR>

" NERD Commenter => Alt + /
map <A-/> <plug>NERDCommenterToggle

" Indent Movement => Alt + [, ]
map <A-]> >>
map <A-[> <<

" Fold codes => Alt + ', Alt + Shift + '
map <A-'> zf
map <A-"> zo

" Manage coc extensions => space + e
nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>

" Show coc commands => space + c
nnoremap <silent> <space>c  :<C-u>CocList commands<cr>

" Autostart NERDTree
autocmd VimEnter * NERDTree

" And then focus on file
autocmd VimEnter * wincmd p

" Open new tab in NERDTree's buffer
autocmd BufWinEnter * NERDTreeMirror

" Autoclose NERDTree
autocmd BufEnter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Start interactive EasyAlign in visual mode (e.g. vipga)
xmap ga <Plug>(EasyAlign)
" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)

" Not to create swap files
set nobackup

set laststatus=2                          " Enables the status line at the bottom of Vim
let g:git_branch_status_head_current=1    " Display only the current branch

let g:NERDTreeGitStatusWithFlags = 1
let g:WebDevIconsUnicodeDecorateFolderNodes = 1
let g:NERDTreeGitStatusNodeColorization = 1
let g:NERDTreeColorMapCustom = {
            \ "Staged"    : "#0ee375",
            \ "Modified"  : "#d9bf91",
            \ "Renamed"   : "#51C9FC",
            \ "Untracked" : "#FCE77C",
            \ "Unmerged"  : "#FC51E6",
            \ "Dirty"     : "#FFBD61",
            \ "Clean"     : "#87939A",
            \ "Ignored"   : "#808080"
            \ }

let g:NERDTreeIgnore = ['^node_modules$','\.pyc$', '^__pycache__$', '\~$']

let NERDTreeStatusline="%{exists('b:NERDTree')?fnamemodify(b:NERDTree.root.path.str(), ':~'):''}"

" Vim Theme set-up => https://github.com/vim-airline/vim-airline-themes/tree/master/autoload/airline/themes
let g:airline_theme = 'base16_gruvbox_dark_hard'

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
let g:airline#extensions#tabline#fnamemod = ':t'          " vim-airline 버퍼 목록 파일명만 출력
let g:airline#extensions#tabline#buffer_nr_show = 1       " buffer number를 보여준다
let g:airline#extensions#tabline#buffer_nr_format = '%s:' " buffer number format
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '>>>'
let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#default#layout = [
            \ [ 'a', 'b', 'c'],
            \ [ 'z']
            \ ]

colorscheme gruvbox

" Auto Completion set-ups
let g:deoplete#enable_at_startup = 1

autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif

inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"

let g:jedi#completions_enabled = 0 " disable autocompletion, cause we use deoplete for completion
let g:jedi#use_splits_not_buffers = "right" " open the go-to function in split, not another buffer

" Vim Pylint set-ups
let g:neomake_python_enabled_makers = ['pylint']
call neomake#configure#automake('nrwi', 500)

"GraphQL Syntax
au BufNewFile,BufRead *.prisma setfiletype graphql

" vim-prettier
" let g:prettier#quickfix_enabled = 0
" let g:prettier#quickfix_auto_focus = 0
" prettier command for coc
command! -nargs=0 Prettier :CocCommand prettier.formatFile
" run prettier on save
" let g:prettier#autoformat = 0
" autocmd BufWritePre *.js,*.jsx,*.mjs,*.ts,*.tsx,*.css,*.less,*.scss,*.json,*.graphql,*.md,*.vue,*.yaml,*.html PrettierAsync

" ctrlp
let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']

" j/k will move virtual lines (lines that wrap)
noremap <silent> <expr> j (v:count == 0 ? 'gj' : 'j')
noremap <silent> <expr> k (v:count == 0 ? 'gk' : 'k')

set number

" Indent set-ups
set smartindent
set autoindent
set cindent

" Tab set-ups
set smarttab
set expandtab
set tabstop=4
set shiftwidth=4

" Encoding set-ups
set enc=utf-8
set fenc=utf-8
set termencoding=utf-8

" Searching set-ups
set hlsearch
set ignorecase

" Disable built-in completion set-up
set nocompatible

" Enable copy/paste set-up
set clipboard=unnamed

set title
set wrap
set linebreak
set showmatch
set cursorline
set mouse=r
set laststatus=2

set listchars=tab:>·
set listchars+=trail:·
set listchars+=extends:»
set listchars+=precedes:«
set listchars+=nbsp:·
set listchars+=space:·

" sync open file with NERDTree
" Check if NERDTree is open or active
function! IsNERDTreeOpen()
    return exists("t:NERDTreeBufName") && (bufwinnr(t:NERDTreeBufName) != -1)
endfunction

" Call NERDTreeFind if NERDTree is active, current window contains a modifiable
" file, and we're not in vimdiff
function! SyncTree()
    if &modifiable && IsNERDTreeOpen() && strlen(expand('%')) > 0 && !&diff
        NERDTreeFind
        wincmd p
    endif
endfunction

" Highlight currently open buffer in NERDTree
autocmd BufEnter * call SyncTree()

" coc config
let g:coc_global_extensions = [
            \ 'coc-snippets',
            \ 'coc-pairs',
            \ 'coc-tsserver',
            \ 'coc-eslint',
            \ 'coc-prettier',
            \ 'coc-json',
            \ ]

" from readme
" if hidden is not set, TextEdit might fail.
" set hidden
" Some servers have issues with backup files,
" see #649 set nobackup set nowritebackup
" Better display for messages set cmdheight=2
" You will have bad experience for diagnostic messages when it's default 4000.
" set updatetime=300

" don't give |ins-completion-menu| messages.
set shortmess+=c

" always show signcolumns
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
" inoremap <silent><expr> <TAB>
            "\ pumvisible() ? "\<C-n>" :
            "\ <SID>check_back_space() ? "\<TAB>" :
            "\ coc#refresh()
" inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
    let col = col('.') - 1
    return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion. => not working
" inoremap <silent><expr> <NUL> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
" inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[g` and `]g` to navigate diagnostics
" nmap <silent> [g <Plug>(coc-diagnostic-prev)
" Show diagnostics => Alt + x
nmap <silent> <A-x> <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)

" Move cursor to definition => Alt + s
nmap <silent> <A-s> <Plug>(coc-definition)
" Show references => Alt + a
nmap <silent> <A-a> <Plug>(coc-references)

" Preview documentation
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
    if (index(['vim','help'], &filetype) >= 0)
        execute 'h '.expand('<cword>')
    else
        call CocAction('doHover')
    endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Rename variable => Alt + v
nmap <A-v> <Plug>(coc-rename)

" Remap for format selected region
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

" NERDTree not to display unnecessary files
augroup nerdtree_open
    autocmd!
    autocmd VimEnter * NERDTree | wincmd p
augroup END

augroup mygroup
    autocmd!
    " Setup formatexpr specified filetype(s).
    autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
    " Update signature help on jump placeholder
    autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <leader>ac  <Plug>(coc-codeaction)
" Fix autofix problem of current line
nmap <leader>qf  <Plug>(coc-fix-current)

" Create mappings for function text object, requires document symbols feature of languageserver.
xmap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap if <Plug>(coc-funcobj-i)
omap af <Plug>(coc-funcobj-a)


" Use `:Format` to format current buffer
command! -nargs=0 Format :call CocAction('format')

" Use `:Fold` to fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" use `:OR` for organize import of current buffer
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add status line support, for integration with other plugin, checkout `:h coc-status`
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Using CocList
" Show all diagnostics
" nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
" Manage coc extensions => space + e
" nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
" Show coc commands => space + c
" nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document
" nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols
" nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
" nnoremap <silent> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
" nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list
" nnoremap <silent> <space>p  :<C-u>CocListResume<CR>l
