<a name="module_TradeValidator"></a>

## TradeValidator
Utility module for validating trades


* [TradeValidator](#module_TradeValidator)
    * [validateTrade(trade)](#exp_module_TradeValidator--validateTrade)
    * [tradeHasAllNecessaryProperties(trade)](#exp_module_TradeValidator--tradeHasAllNecessaryProperties)
    * [tradeHasNoUndefinedProperties(trade)](#exp_module_TradeValidator--tradeHasNoUndefinedProperties)
    * [checkTradeHasAllProperties(trade)](#exp_module_TradeValidator--checkTradeHasAllProperties)
    * [checkTradeFullyDefined(trade)](#exp_module_TradeValidator--checkTradeFullyDefined)
    * [tradeIDisValid(tradeID)](#exp_module_TradeValidator--tradeIDisValid)
    * [dateOfTradeIsValid(date)](#exp_module_TradeValidator--dateOfTradeIsValid)
    * [productQuantityIsValid(quantity)](#exp_module_TradeValidator--productQuantityIsValid)
    * [productPriceIsValid(price)](#exp_module_TradeValidator--productPriceIsValid)
    * [stringLengthIsValid(stringField)](#exp_module_TradeValidator--stringLengthIsValid)
    * [currencyCodeIsValid(code)](#exp_module_TradeValidator--currencyCodeIsValid)

<a name="exp_module_TradeValidator--validateTrade"></a>

### validateTrade(trade)
Validates the fields of the derivative trade one-by-one to be valid at basic level.
Throws an exception if any fields are invalid.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| trade | <code>Object</code> | Object representing a trade entry |

<a name="exp_module_TradeValidator--tradeHasAllNecessaryProperties"></a>

### tradeHasAllNecessaryProperties(trade)
Returns true if the trade has all attributes necessary.
Throws an exception with an error listing the missing fields otherwise.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| trade | <code>Object</code> | Derivative trade |

<a name="exp_module_TradeValidator--tradeHasNoUndefinedProperties"></a>

### tradeHasNoUndefinedProperties(trade)
Returns true if all the attributes of the input object are defined
 i.e no attributes have the value `undefined`.
Throws an exception listing undefined attributes otherwise.
Note: Will return true for the empty object {}.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| trade | <code>Object</code> | Derivative trade |

<a name="exp_module_TradeValidator--checkTradeHasAllProperties"></a>

### checkTradeHasAllProperties(trade)
Returns true if the object has all the necessary trade attributes.
Similar to `tradeHasAllNecessaryProperties`, except returns false
if an attribute is not found instead of throwing an exception.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| trade | <code>Object</code> | derivative trade |

<a name="exp_module_TradeValidator--checkTradeFullyDefined"></a>

### checkTradeFullyDefined(trade)
Returns true of all the attributes of the input object are defined 
i.e none of the attributes of the object have the value `undefined`
or the object is empty ({}).
Returns false otherwise.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| trade | <code>Object</code> | Derivative trade |

<a name="exp_module_TradeValidator--tradeIDisValid"></a>

### tradeIDisValid(tradeID)
Returns true if the trade ID matches a set of capital letters
[A-Z] followed by a set of digits [0-9].
Does not check if the trade ID exists in the database

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| tradeID | <code>number</code> | Trade ID number |

<a name="exp_module_TradeValidator--dateOfTradeIsValid"></a>

### dateOfTradeIsValid(date)
Returns true if the input string can successfully be parsed into a date.
False otherwise.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| date | <code>string</code> | Date string representation |

<a name="exp_module_TradeValidator--productQuantityIsValid"></a>

### productQuantityIsValid(quantity)
Returns true if the quantity value can be parsed into an integer
and is non-zero.

**Kind**: Exported function  

| Param | Type |
| --- | --- |
| quantity | <code>number</code> | 

<a name="exp_module_TradeValidator--productPriceIsValid"></a>

### productPriceIsValid(price)
Returns true if the price value can be parsed into a float and is non-zero.

**Kind**: Exported function  

| Param | Type |
| --- | --- |
| price | <code>number</code> | 

<a name="exp_module_TradeValidator--stringLengthIsValid"></a>

### stringLengthIsValid(stringField)
Returns true if the string value is defined, non-empty 
and at most 200 chars in length.

**Kind**: Exported function  

| Param | Type |
| --- | --- |
| stringField | <code>string</code> | 

<a name="exp_module_TradeValidator--currencyCodeIsValid"></a>

### currencyCodeIsValid(code)
Returns true if the input code is included in the set of currencies 
provided by the test data.

**Kind**: Exported function  

| Param | Type | Description |
| --- | --- | --- |
| code | <code>string</code> | 3 Letter ISO currency code |

