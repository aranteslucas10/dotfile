filetype plugin indent on 
syntax on 

set nocompatible 
set number
set relativenumber
set mouse=a
set wildmenu
set splitbelow
set splitright
set showcmd
set laststatus=2           " Always show statusline.
set ttyfast                " Faster redrawing.
set lazyredraw             " Only redraw when necessary.
set tb= 		   " "icons", "text" and/or "tooltips"; how to show the toolbar
set hidden                 " Trocar de buffer sem salvar"
set hlsearch               " Todos matchs marcados"
set incsearch              " Pinta de acordo com a pesquisa"
set termguicolors

nmap \f gg<C-v>GI'<esc>A<esc><C-v>G$A'<esc>A<esc><C-v>G$kA,<esc>ggI(<esc>GA)<esc>

highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/

autocmd! BufWritePost ~/.vimrc source %

" Specify a directory for plugins
" - For Neovim: ~/.local/share/nvim/plugged
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')
Plug 'nvie/vim-flake8'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'tpope/vim-fugitive'
" Plug 'python-mode/python-mode', { 'branch': 'develop' }
Plug 'tpope/vim-commentary'
Plug 'makerj/vim-pdf'
Plug 'vim-scripts/c.vim'
" Plug 'xavierchow/vim-swagger-preview'
Plug 'tomasr/molokai'
Plug 'vim-scripts/Wombat'
Plug 'ajh17/spacegray.vim'
Plug 'fenetikm/falcon'
" Plug 'fholgado/minibufexpl.vim'
Plug 'jeetsukumaran/vim-buffergator'
Plug 'romgrk/winteract.vim'
Plug 'muansari96/vimify'
Plug 'itchyny/lightline.vim' 
Plug 'scrooloose/nerdtree' 
call plug#end()
" colorscheme dracula
" colorscheme industry
" colorscheme falcon
colorscheme molokai
" colorscheme spacegray
" Cola o que estiver no clipboard no terminal em foco utilizando Ctrl-V
tnoremap <C-v> <C-w>:call term_sendkeys("%", @+)<CR>
" Faz com que a transição entre command-line e normal-mode seja instantanea
set ttimeoutlen=0

set clipboard=unnamedplus " y to clipboard

set guioptions-=m  "remove menu bar
set guioptions-=T  "remove toolbar
set guioptions-=r  "remove right-hand scroll bar
set guioptions-=L  "remove left-hand scroll bar

" map <silent> <F11>:call system("wmctrl -ir " . v:windowid . " -b toggle,fullscreen")<CR>

" Spotify map
map <Leader>s :SpToggle<CR>

let g:lightline = {
			\'colorscheme': 'molokai',
			\'active': {
			\     'left': [ [ 'mode', 'filename', 'paste' ], [ 'status_case' ] ]
			\},
			\'component_function': {
			\ 'status_case': 'StatusCase',
			\}}
function! StatusCase()
	return g:minha_variavel_global
endfunction

let g:minha_variavel_global = ""

" NERDtree configurações
map <leader>e :NERDTreeToggle<CR>

