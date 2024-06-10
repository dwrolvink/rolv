local autocmd = vim.api.nvim_create_autocmd

-- don't auto comment new lines
vim.cmd([[autocmd FileType * set formatoptions-=ro]])

-- enable copy to clipboard
vim.api.nvim_set_option("clipboard", "unnamed")

-- Ctrl-Insert  = Copy
vim.keymap.set('v', '<C-Insert>', '"+y', { desc='Copy' })
