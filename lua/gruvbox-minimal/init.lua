local M = {}

M.config = {
    transparent = false,
    italic_comments = false,
    contrast = "low",
    theme = "dark",
    accent = "red",
}

function M.setup(opts)
	M.config = vim.tbl_deep_extend("force", M.config, opts or {})
end

function M.load()
	local palette = require("gruvbox-minimal.palette").get(M.config.contrast, M.config.theme)
	local groups = require("gruvbox-minimal.groups").setup(palette, M.config)

	for group, settings in pairs(groups) do
		vim.api.nvim_set_hl(0, group, settings)
	end
end

return M
