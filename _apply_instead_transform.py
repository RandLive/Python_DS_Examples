# =============================================================================
# Other transformations with .apply
# =============================================================================


# apply和transform的不同之处在于，apply是面对选定序列，而transform是面对全部。
# link: http://blog.csdn.net/elecjack/article/details/50760736

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])