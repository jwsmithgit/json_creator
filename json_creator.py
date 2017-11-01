#!/usr/bin/env python3

# PACKAGES
import os.path
import json


######## TYPE HANDLERS
def string_to_type( string, type_ ):
    if not string:
        return None
    if type_ == 'int':
        return int( string )
    if type_ == 'float':
        return float( string )
    if type_ == 'bool':
        if string.lower() == 'true':
            return True
        if string.lower() == 'False':
            return False
    if type_ == 'str':
        return string
    return None

def string_to_type_string( string ):
    if is_list( string ):
        return 'list'
    if is_dict( string ):
        return 'dict'
    if is_int( string ):
        return 'int'
    if is_float( string ):
        return 'float'
    if is_bool( string ):
        return 'bool'
    if is_str( string ):
        return 'str'
    return False

def string_is_type( string, type_ ):
    if type_ == 'list' and is_list( string ):
        return True
    if type_ == 'dict' and is_dict( string ):
        return True
    if type_ == 'int' and is_int( string ):
        return True
    if type_ == 'float' and is_float( string ):
        return True
    if type_ == 'bool' and is_bool( string ):
        return True
    if type_ == 'str' and is_str( string ):
        return True
    return False

def is_bool( value ):
    bool_str = ( 'true', 'false' )
    if str(value) in bool_str:
        return True
    return False

def is_int( value ):
    int_str = ( 'i','int' )
    if value in int_str:
        return True

    try:
        int( value )
        return True
    except:
        return False

def is_float( value ):
    float_str = ( 'f','float' )
    if value in float_str:
        return True

    try:
        float( value )
        return True
    except:
        return False

def is_str( value ):
    str_str = ( 's','str','string' )
    if value in str_str:
        return True

    return True

def is_list( value ):
    list_str = ( '[]','l','list' )
    if value in list_str:
        return True

    if value.startswith( '[]' ) or value.endswith( '[]' ):
        return True
    if value.startswith( '[' ) and value.endswith( ']' ):
        return True
    return False

def is_dict( value ):
    dict_str = ( '{}','d','dict' )
    if value in dict_str:
        return True

    if value.startswith( '{}' ) or value.endswith( '{}' ):
        return True
    if value.startswith( '{' ) and value.endswith( '}' ):
        return True
    return False

def string_to_type_list( string ):
    if len( string ) <= 2:
        return []
    if string.startswith( '[]' ):
        return [ string[2:] ]
    if string.endswith( '[]' ):
        return [ string[:-2] ]
    if string.startswith( '[' ) and s.endswith( ']' ):
        return [ string[1:-1] ]
    return []

def string_to_type_dict( string ):
    if len( string ) <= 2:
        return {}
    if string.startswith( '{}' ):
        return { '_type': string[2:] }
    if string.endswith( '{}' ):
        return { '_type': string[:-2] }
    if string.startswith( '{' ) and string.endswith( '}' ):
        return { '_type': string[1:-1] }
    return {}


######## JSON HANDLERS

# Load Json data from file
def load_json( filename ):
    with open( filename ) as data_file:
        data = json.load( data_file )
    return data

# Save object to file
def save_json( filename, data ):
    with open( filename, 'w' ) as out_file:
        json.dump( data, out_file, sort_keys=True, indent=4, separators=( ',', ': ' ) )
    return


######## FILE HANDLERS

# Handle file stuff
def file_setup(  ):
    filename = get_filename(  )

    if not file_exists( filename ):
        init_file( filename )

    return filename

# Get filename input
def get_filename(  ):
    print( 'ENTER JSON DATAFILE. ' )
    filename = input(  )
    print( '' )

    filename = fix_filename( filename )
    return filename

# Appends .json if not there
def fix_filename( filename ):
    if not filename.endswith( '.json' ):
        filename += '.json'
    return filename

# Checks if file exists
def file_exists( filename ):
    return os.path.isfile( filename )

# Initialize file for JSON
def init_file( filename ):
    file = open( filename, 'w' )
    file.write( '[\n]' )
    file.close(  )
    return



######## INPUT HELPERS

def is_valid( value ):
    if get_value_str_type( value ) or get_type_str_type( value ):
        return True
    return False

def fix_input( value ):
    return value.replace( ' ','' )

def is_exit_value( value ):
    exit_values = ( 'q' ) #,'quit','e','exit'
    if value and str(value) in exit_values:
        return True
    return False


######## MENU
def menu_handler(  ):

    print( '---WELCOME TO JSON CREATOR---' )
    print( '' )
    print( '1: Add entities. ' )
    print( '2: View entities. ' )
    print( '' )
    print( '4: Modify entities. ' )
    print( '5: Remove entities. ' )
    print( '6: Cleanup entities. ' )
    print( '' )
    print( '9: Help. ' )
    print( '0: Exit. ' )
    print( '' )

    while 1:
        option = input(  )
        print( '' )

        if is_int( option ):
            option = int( option )
            if option in (1,2,4,5,6,9,0):
                return option

        print( 'that is not an option. ' )
        print( '' )

    return

# STRING DICTATES FUNCTION
def option_handler( option, filename ):
    print( '' )
    if( option == 1 ):
        print( '-ADDING-' )
        print( '' )
        add( filename )
    elif( option == 2 ):
        print( '-VIEWING-' )
        print( '' )
        view( filename )
    elif( option == 4 ):
        print( '-MODIFYING-' )
        print( '' )
        modify( filename )
    elif( option == 5 ):
        print( '-REMOVING-' )
        print( '' )
        remove( filename )
    elif( option == 6 ):
        print( '-CLEANING-' )
        print( '' )
        clean( filename )
    elif( option == 9 ):
        print( '-HELPING-' )
        print( '' )
        help()
    elif( option == 0 ):
        print( '-EXITING-' )
        print( '' )

    return


######## PRINT HANDLERS
def print_indent( indent ):
    for x in range( indent ):
        print ( '  ', end = '' )
    return

def indent_string( indent ):
    string = ''
    for x in range( indent ):
        string += '  '
    return string

def print_data( data, indent = 0, name = None ):
    print_indent( indent )

    if name:
        print( str(name) + ': ', end='' )

    first_entry = False
    if indent == 0:
        first_entry = True

    if isinstance( data, list ):

        print( '[', end='' )
        comma = False
        for item in data:
            if comma:
                print( ',', end='' )
            print( '' )
            print_data( item, indent+1 )
            print( '' )
            comma = True

        print( '' )
        print( indent_string( indent ) + ']', end='' )
        return

    if isinstance( data, dict ):
        if not first_entry:
            print( '{', end='' )

        comma = False
        for name in sorted(data):
            if comma:
                print( ',', end='' )

            if not first_entry or comma:
                print('')

            print_data( data[name], indent+1, name )
            comma = True

        print('')

        if not first_entry:
            print( indent_string( indent ) + '}', end = '' )
        return

    print( str( data ), end='' )
    return



######## INPUT HANDLERS
def name_input(  ):
    print( '' )
    print( 'ENTER VALUE NAME. ' )
    name = '_id'

    while not name or name == '_id':
        name = input( '' )

    return name


def type_input(  ):
    print( '' )
    print( 'ENTER VALUE TYPE. types: i, f, s, [], {}; or input sample. ' )
    type_ = ''

    type_input = input( '' )
    type_ = string_to_type_string( type_input )
    if not type_input:
        return

    if type_ == 'list':
        type_ = string_to_type_list( type_input )
        if not type_:
            type_ = type_list_input(  )

    if type_ == 'dict':
        type_ = string_to_type_dict( type_input )
        if not type_:
            type_ = type_dict_input(  )

    return type_


def value_input( type_, name='', indent=0 ):
    print_indent( indent )

    if name:
        print( name + ': ', end='' )

    if isinstance( type_, list ):
        print( 'list' )
        value = value_list_input( type_, indent=indent+1 )
    elif isinstance( type_, dict ):
        print( 'dict' )
        value = value_dict_input( type_, indent=indent+1 )
    else:
        print( type_ )
        print( '' )
        print( indent_string( indent ) + 'ENTER VALUE. ' )

        while 1:
            value = input( indent_string( indent ) )
            if is_exit_value( value ):
                return value
            if not value or string_is_type(value, type_):
                break

            print( '' )
            print( indent_string( indent ) + 'incorrect value type. ')
            print( '' )
            print( indent_string( indent ) + 'type is ' + type_ + '. ' )

        value = string_to_type( value, type_ )

    return value


def value_list_input( type_list, indent=0 ):
    print( 'CREATING LIST. ' )
    list_ = []
    type_ = type_list[0]

    while 1:
        value = value_input( type_, indent )
        if is_exit_value(value):
            return list_

        list.append( value )

    return []


def value_dict_input( type_dict, indent=0 ):
    dict_ = {}
    exiting = False

    # has shared type
    if 'type_' in type_dict:
        type_ = type_dict[ 'type_' ]
        while 1:
            name = name_input()

            exiting = is_exit_value(name)
            if not exiting:
                value = value_input( type_, name, indent )

                exiting = is_exit_value(value)
                if not exiting:
                    dict_[ name ] = value

            if exiting:
                break

    # has specified types
    else:
        for name in sorted( type_dict ):
            if not exiting:
                type_ = type_dict[ name ]
                value = value_input( type_, name, indent )

                exiting = is_exit_value(value)

            if exiting:
                # @DOES NOT SAVE DICTIONARY< WOULD LIKE TO IF DICTIS PARTLY FILLED
                return 'q'

                # some values were set so set the rest to None
                """if dict_:
                    dict_[ name ] = None"""
                # no dictionary made yet, so just exit
                """else:
                    return 'q'"""
            else:
                dict_[ name ] = value

    return dict_


def type_list_input( ):
    print( 'CREATING TYPE LIST. ' )
    list_ = []

    type_ = type_input()
    if type_:
        list_.append( type_ )

    return list_



# creates a core dict object
def type_dict_input( ):
    print( 'CREATING TYPE SET. ' )
    dict_ = {}

    while 1 :
        name = name_input()
        if is_exit_value( name ):
            return dict_

        type_ = type_input()
        if type_:
            dict_[ name ] = type_

    return {}

def get_id( entity ):
    return entity['_id']

# goes wrong if data isnt sorted. currently stays sorted via save_json FUNCTION
# if user edits order in txt. fucks up.
def entity_number( data ):

    for entity,i in zip( data,range( len(data) ) ):
        if i != entity["_id"]:
            return i

    return len(data)



######## ADD
def add( filename ):
    data = load_json( filename )

    if not data:
        print( "there is no data. ")

        core = create_core()
        if not core:
            print( "there is no core. ")
            return

        data.append( core )
        save_json( filename, data )
    else:
        core = data[0]

    print( '' )
    print( 'core.' )
    print_data( core )

    while 1:
        entity = create_entity( core )
        if not entity:
            return

        entity[ '_id' ] = entity_number( data )
        data.append( entity )
        save_json( filename, data )

        print( '' )
        print( 'entity.' )
        print_data( entity )

    return

def create_core(  ):
    print( 'CREATING CORE. ')
    core = type_dict_input()
    if not core:
        print( "no data entered. no core created. ")
        return {}

    core[ '_id' ] = 0
    return core

def create_entity( core ):
    print( '' )
    print( '' )
    print( 'CREATING ENTITY. ')
    print( '' )
    entity = {}

    for name in sorted( core ):
        if name == '_id':
            continue

        type_ = core[ name ]

        value = value_input( type_, name, 1 )
        if is_exit_value( value ):
            return entity

        entity[ name ] = value

    return entity


def filter_input( core, name='', indent=0 ):
    print_indent( indent )

    while 1:
        name = name_input()

        if not name or is_exit_value( name ):
            return filter_
        if name in core:
            break
    if name:
        print( name + ': ', end='' )

    if isinstance( core, list ):
        print( 'list' )
        value = name_value_list_input( core, indent=indent+1 )
    elif isinstance( core, dict ):
        print( 'dict' )
        value = filter_value_input( type_, indent=indent+1 )
    else:
        print( type_ )
        print( '' )
        print( indent_string( indent ) + 'ENTER VALUE. ' )

        while 1:
            value = input( indent_string( indent ) )
            if is_exit_value( value ):
                return value
            if not value or string_is_type(value, type_):
                break

            print( '' )
            print( indent_string( indent ) + 'incorrect value type. ')
            print( '' )
            print( indent_string( indent ) + 'type is ' + type_ + '. ' )

        value = string_to_type( value, type_ )

    return value


def name_value_list_input( ):
    print( 'CREATING TYPE LIST. ' )
    list_ = []

    type_ = type_input()
    if type_:
        list_.append( type_ )

    return list_



# creates a core dict object
def name_value_dict_input( ):
    print( 'CREATING TYPE SET. ' )
    dict_ = {}

    while 1 :
        name = name_input()
        if is_exit_value( name ):
            return dict_

        type_ = type_input()
        if type_:
            dict_[ name ] = type_

    return {}

# VIEW
def create_filter( core ):
    print( '\nCREATING FILTER. ')
    # create filter
    # empty filter is no filter
    filter_ = {}

    filter_input( core )

    value = name_value_input( core[name] )
    filter_[ name ] = value

    return filter_


def is_subset( data1, data2 ):
    if isinstance( data1, list ):
        for item1 in data1:

            for item2 in data2:
                if is_subset( item1, item2 ):
                    return True

            return False

    elif isinstance( data1, dict ):
        for name in data1:

            if is_subset( data1[name], data2[name] ):
                return True

            return False

    else:
        if data1 == data2 or data1 == None:
            return True
        return False


def view( filename ):

    data = load_json( filename )

    if not data:
        print( 'no data file exists. ' )
        return

    core = data[0]
    if not core:
        print( 'sorry, no core exists. ' )
        return

    filter_ = create_filter( core )

    # print with filter
    print( '' )
    print( 'NOW VIEWING. ' )

    if filter_:
        for entity in data:
            if is_subset( filter_, entity ):
                print( 'entity. ' )
                print_data( entity )
    else:
        for entity in data[1:]:
            print( '' )
            print( 'entity. ' )
            print( '' )
            print_data( entity )

    input(  )

    return



# MODIFY
def modify_core( file_name ):
    json_data = load_json( file_name )
    if not json_data:
        return

    core_entity = json_data[0]
    while 1:
        name = ''
        value = ''
        vtype = ''
        is_list = False

        # GET NAME OF VALUE
        print_info( 'name' )
        print( '' )
        name = get_name()
        print( '' )

        # q to exit
        if name == 'q':
            break

        # GET VALUE
        print( 'ENTER VALUE. ' )
        print( '[]:list. type:str,int,sample. ' )
        value = value_input()


        # DETECT LIST, different ways of entity
        # 1: before value, 2: after value, 3: around value
        value.replace(" ", "")
        is_list = check_array_format( value )

        vtype = get_value_str_type( value )
        # ADJUST VALUE TYPE IF LIST
        if is_list:
            vtype = (list,vtype)

        # PRINT INFO ON PARSE
        print( 'CAPTURED TYPE: ' + str(vtype) + '.' )
        print( '' )

        #APPEND TO CORE ENTITY
        core_entity[name] = vtype

        #ADD ENTITY TO DATA
        if json_data:
            json_data[0] = core_entity
        else:
            json_data.append( core_entity )
        save_json( file_name, json_data )


    print( 'CORE ENTITY CREATED. ' )
    print( '' )
    return

def modify_core_remove( file_name ):
    json_data = load_json( file_name )
    if not json_data:
        return

    core_entity = json_data[0]

    while 1 :
        print( 'CORE. ' )
        for field in core_entity:
            print( str(field) + ' - ' + str(core_entity[field]) )
        print( '' )

        print_info( 'name' )
        print( '' )
        name = get_name()

        if name == 'q' : return

        for entity in json_data:
            if name in entity:
                del entity[name]

        save_json( file_name, json_data )

    return


'''def clone_core( data_from, data_to ):
    if isinstance( data_from, list ):
        for item_to in data_to:
            clone_core(  )


    elif isinstance( from_data, dict ):
        for name

    else :
        to_data = None

    return to_data
'''

# VIEW
def create_filter2( core ):
    print( '\nCREATING FILTER. ')
    # create filter
    # empty filter is no filter
    filter_ = {}
    while 1:
        while 1:
            name = name_input()

            if not name or is_exit_value( name ):
                return filter_
            if name in core:
                break

        value = value_input( core[name] )
        filter_[ name ] = value

    return filter_

def empty_clone( data ):
    if isinstance( data, list ):
        list_ = []
        for item in data:
            list_.append( empty_clone( item ) )
        return list_

    elif isinstance( data, dict ):
        dict_ = {}
        for name in data:
            dict_[name] = empty_clone( data[name] )
        return dict_

    else :
        return None

# REMOVE
def remove( file_name ):
    data = load_json( file_name )
    if not data:
        return

    core = data[0]

    #create filter
    filter_ = create_filter( core )
    print( filter_ )
    print( '' )
    print( core )
    #filter_ = create_filter( core )

    for entity in core( data[1:] ):
        if is_subset( filter_, entity ):
            del entity

    return


# CLEAN
def fill_empty( data, core, indent=1 ):
    if data == None:
        print('')
        data = value_input( core, indent=indent-1 )

    elif isinstance( data, list ):
        print( indent_string(indent) + 'list' )
        if not data:
            data = value_input( core[0] )

        else:
            for item_d, item_c  in zip( sorted(data), sorted(core) ):
                item_d = fill_empty( item_d, item_c, indent=indent+1 )


    elif isinstance( data, dict ):
        print( ' - dict' )
        for name_d, name_c in zip( sorted(data), sorted(core)):
            print(  indent_string(indent) + name_d, end='' )
            data[name_d] =  fill_empty( data[name_d], core[name_c], indent=indent+1 )
            print( '' )

    return data


def clean( file_name ):
    data = load_json( file_name )

    if not data:
        print( "there is no data. ")
        return

    core = data[0]

    for entity in data[1:]:
        fill_empty( entity, core )

        save_json( file_name, data )
        print( 'entity saved.' )
        print( 'next entity. ' )
        print( '' )

    return


# HELP
def help():
    print( 'INSERT HELP HERE' )
    print( '' )
    return

# EXIT



def main(  ):
    print( '' )
    filename = file_setup(  )

    while 1:
        option = menu_handler(  )
        if option == 0:
            break

        option_handler( option, filename )
        print( "")

    return


if __name__ == '__main__':
    main(  )
