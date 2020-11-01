## c5-3
- 如果出现 decode错误 需要到venv/Lib/site-packages/pip/compat 里面进行修改, 大概在代码75行, s.decode('utf-8') 改成 'gbk'
- 卸载: pip uninstall coreapi MarkupSafe
- 然后重新安装 coreapi 

## c7-7
    不集成短信验证功能