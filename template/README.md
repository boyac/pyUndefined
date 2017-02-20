1. import Mapping() class as m
2. Configure read and write excel as input and output source.
3. Define the range you of both input and output for copy and paste, including '
  - tables, 
  - fields,
  - type
  - length
  - logic (if any)


```
# Example

if __name__ == '__main__':
	
	m = Mapping()
	#get current active sheet's name
	#active = xw.Book('TFB_MAPPING_JS.xlsx').sheets.active.name

	def table_1():
		read = m.excel_config_r('TFB_MAPPING_JS.xlsx', 'MINIPORT_GL_110_TW (fr HQBB)')
		write = m.excel_config_w('ETL_BC.xlsm', 'Field List')
		
		#tables
		m.excel_read(read,'D2:D25')
		m.excel_write(write,'A2107:A2130')

		#fields
		m.excel_read(read,'E2:E25')
		m.excel_write(write,'D2107:D2130')
		
		#type
		m.excel_read(read, 'F2:F25')
		m.excel_write(write, 'E2107:E2130')

		#length
		m.excel_read(read, 'G2:G25')
		m.excel_write(write, 'F2107:F2130')

		#logic
		#m.excel_read(read,'D2:D25')
		#m.excel_write(write,'D2107:D2130')

```
