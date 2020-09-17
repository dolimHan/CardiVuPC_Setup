// generatedy by JSX compiler 0.9.89 (2014-05-20 06:01:03 +0900; 8e8c6105f36f3dfe440ea026a3c93a3444977102)
var JSX = {};
(function (JSX) {
/**
 * extends the class
 */
function $__jsx_extend(derivations, base) {
	var ctor = function () {};
	ctor.prototype = base.prototype;
	var proto = new ctor();
	for (var i in derivations) {
		derivations[i].prototype = proto;
	}
}

/**
 * copies the implementations from source interface to target
 */
function $__jsx_merge_interface(target, source) {
	for (var k in source.prototype)
		if (source.prototype.hasOwnProperty(k))
			target.prototype[k] = source.prototype[k];
}

/**
 * defers the initialization of the property
 */
function $__jsx_lazy_init(obj, prop, func) {
	function reset(obj, prop, value) {
		delete obj[prop];
		obj[prop] = value;
		return value;
	}

	Object.defineProperty(obj, prop, {
		get: function () {
			return reset(obj, prop, func());
		},
		set: function (v) {
			reset(obj, prop, v);
		},
		enumerable: true,
		configurable: true
	});
}

var $__jsx_imul = Math.imul;
if (typeof $__jsx_imul === "undefined") {
	$__jsx_imul = function (a, b) {
		var ah  = (a >>> 16) & 0xffff;
		var al = a & 0xffff;
		var bh  = (b >>> 16) & 0xffff;
		var bl = b & 0xffff;
		return ((al * bl) + (((ah * bl + al * bh) << 16) >>> 0)|0);
	};
}

/**
 * fused int-ops with side-effects
 */
function $__jsx_ipadd(o, p, r) {
	return o[p] = (o[p] + r) | 0;
}
function $__jsx_ipsub(o, p, r) {
	return o[p] = (o[p] - r) | 0;
}
function $__jsx_ipmul(o, p, r) {
	return o[p] = $__jsx_imul(o[p], r);
}
function $__jsx_ipdiv(o, p, r) {
	return o[p] = (o[p] / r) | 0;
}
function $__jsx_ipmod(o, p, r) {
	return o[p] = (o[p] % r) | 0;
}
function $__jsx_ippostinc(o, p) {
	var v = o[p];
	o[p] = (v + 1) | 0;
	return v;
}
function $__jsx_ippostdec(o, p) {
	var v = o[p];
	o[p] = (v - 1) | 0;
	return v;
}

/**
 * non-inlined version of Array#each
 */
function $__jsx_forEach(o, f) {
	var l = o.length;
	for (var i = 0; i < l; ++i)
		f(o[i]);
}

/*
 * global functions, renamed to avoid conflict with local variable names
 */
var $__jsx_parseInt = parseInt;
var $__jsx_parseFloat = parseFloat;
function $__jsx_isNaN(n) { return n !== n; }
var $__jsx_isFinite = isFinite;

var $__jsx_encodeURIComponent = encodeURIComponent;
var $__jsx_decodeURIComponent = decodeURIComponent;
var $__jsx_encodeURI = encodeURI;
var $__jsx_decodeURI = decodeURI;

var $__jsx_ObjectToString = Object.prototype.toString;
var $__jsx_ObjectHasOwnProperty = Object.prototype.hasOwnProperty;

/*
 * profiler object, initialized afterwards
 */
function $__jsx_profiler() {
}

/*
 * public interface to JSX code
 */
JSX.require = function (path) {
	var m = $__jsx_classMap[path];
	return m !== undefined ? m : null;
};

JSX.profilerIsRunning = function () {
	return $__jsx_profiler.getResults != null;
};

JSX.getProfileResults = function () {
	return ($__jsx_profiler.getResults || function () { return {}; })();
};

JSX.postProfileResults = function (url, cb) {
	if ($__jsx_profiler.postResults == null)
		throw new Error("profiler has not been turned on");
	return $__jsx_profiler.postResults(url, cb);
};

JSX.resetProfileResults = function () {
	if ($__jsx_profiler.resetResults == null)
		throw new Error("profiler has not been turned on");
	return $__jsx_profiler.resetResults();
};
JSX.DEBUG = false;
var GeneratorFunction$0 = 
(function () {
  try {
    return Function('import {GeneratorFunction} from "std:iteration"; return GeneratorFunction')();
  } catch (e) {
    return function GeneratorFunction () {};
  }
})();
var __jsx_generator_object$0 = 
(function () {
  function __jsx_generator_object() {
  	this.__next = 0;
  	this.__loop = null;
	this.__seed = null;
  	this.__value = undefined;
  	this.__status = 0;	// SUSPENDED: 0, ACTIVE: 1, DEAD: 2
  }

  __jsx_generator_object.prototype.next = function (seed) {
  	switch (this.__status) {
  	case 0:
  		this.__status = 1;
  		this.__seed = seed;

  		// go next!
  		this.__loop(this.__next);

  		var done = false;
  		if (this.__next != -1) {
  			this.__status = 0;
  		} else {
  			this.__status = 2;
  			done = true;
  		}
  		return { value: this.__value, done: done };
  	case 1:
  		throw new Error("Generator is already running");
  	case 2:
  		throw new Error("Generator is already finished");
  	default:
  		throw new Error("Unexpected generator internal state");
  	}
  };

  return __jsx_generator_object;
}());
function Among(s, substring_i, result) {
	this.s_size = s.length;
	this.s = s;
	this.substring_i = substring_i;
	this.result = result;
	this.method = null;
	this.instance = null;
}

function Among$0(s, substring_i, result, method, instance) {
	this.s_size = s.length;
	this.s = s;
	this.substring_i = substring_i;
	this.result = result;
	this.method = method;
	this.instance = instance;
}

$__jsx_extend([Among, Among$0], Object);
function Stemmer() {
}

$__jsx_extend([Stemmer], Object);
function BaseStemmer() {
	var current$0;
	var cursor$0;
	var limit$0;
	this.cache = ({  });
	current$0 = this.current = "";
	cursor$0 = this.cursor = 0;
	limit$0 = this.limit = current$0.length;
	this.limit_backward = 0;
	this.bra = cursor$0;
	this.ket = limit$0;
}

$__jsx_extend([BaseStemmer], Stemmer);
BaseStemmer.prototype.setCurrent$S = function (value) {
	var current$0;
	var cursor$0;
	var limit$0;
	current$0 = this.current = value;
	cursor$0 = this.cursor = 0;
	limit$0 = this.limit = current$0.length;
	this.limit_backward = 0;
	this.bra = cursor$0;
	this.ket = limit$0;
};


function BaseStemmer$setCurrent$LBaseStemmer$S($this, value) {
	var current$0;
	var cursor$0;
	var limit$0;
	current$0 = $this.current = value;
	cursor$0 = $this.cursor = 0;
	limit$0 = $this.limit = current$0.length;
	$this.limit_backward = 0;
	$this.bra = cursor$0;
	$this.ket = limit$0;
}

BaseStemmer.setCurrent$LBaseStemmer$S = BaseStemmer$setCurrent$LBaseStemmer$S;

BaseStemmer.prototype.getCurrent$ = function () {
	return this.current;
};


function BaseStemmer$getCurrent$LBaseStemmer$($this) {
	return $this.current;
}

BaseStemmer.getCurrent$LBaseStemmer$ = BaseStemmer$getCurrent$LBaseStemmer$;

BaseStemmer.prototype.copy_from$LBaseStemmer$ = function (other) {
	this.current = other.current;
	this.cursor = other.cursor;
	this.limit = other.limit;
	this.limit_backward = other.limit_backward;
	this.bra = other.bra;
	this.ket = other.ket;
};


function BaseStemmer$copy_from$LBaseStemmer$LBaseStemmer$($this, other) {
	$this.current = other.current;
	$this.cursor = other.cursor;
	$this.limit = other.limit;
	$this.limit_backward = other.limit_backward;
	$this.bra = other.bra;
	$this.ket = other.ket;
}

BaseStemmer.copy_from$LBaseStemmer$LBaseStemmer$ = BaseStemmer$copy_from$LBaseStemmer$LBaseStemmer$;

BaseStemmer.prototype.in_grouping$AIII = function (s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor >= this.limit) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor);
	if (ch > max || ch < min) {
		return false;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0x1 << (ch & 0x7)) === 0) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	return true;
};


function BaseStemmer$in_grouping$LBaseStemmer$AIII($this, s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor >= $this.limit) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor);
	if (ch > max || ch < min) {
		return false;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0x1 << (ch & 0x7)) === 0) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	return true;
}

BaseStemmer.in_grouping$LBaseStemmer$AIII = BaseStemmer$in_grouping$LBaseStemmer$AIII;

BaseStemmer.prototype.in_grouping_b$AIII = function (s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor <= this.limit_backward) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor - 1);
	if (ch > max || ch < min) {
		return false;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0x1 << (ch & 0x7)) === 0) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	return true;
};


function BaseStemmer$in_grouping_b$LBaseStemmer$AIII($this, s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor <= $this.limit_backward) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor - 1);
	if (ch > max || ch < min) {
		return false;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0x1 << (ch & 0x7)) === 0) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	return true;
}

BaseStemmer.in_grouping_b$LBaseStemmer$AIII = BaseStemmer$in_grouping_b$LBaseStemmer$AIII;

BaseStemmer.prototype.out_grouping$AIII = function (s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor >= this.limit) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor);
	if (ch > max || ch < min) {
		($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
		return true;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0X1 << (ch & 0x7)) === 0) {
		($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
		return true;
	}
	return false;
};


function BaseStemmer$out_grouping$LBaseStemmer$AIII($this, s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor >= $this.limit) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor);
	if (ch > max || ch < min) {
		($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
		return true;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0X1 << (ch & 0x7)) === 0) {
		($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
		return true;
	}
	return false;
}

BaseStemmer.out_grouping$LBaseStemmer$AIII = BaseStemmer$out_grouping$LBaseStemmer$AIII;

BaseStemmer.prototype.out_grouping_b$AIII = function (s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor <= this.limit_backward) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor - 1);
	if (ch > max || ch < min) {
		($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
		return true;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0x1 << (ch & 0x7)) === 0) {
		($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
		return true;
	}
	return false;
};


function BaseStemmer$out_grouping_b$LBaseStemmer$AIII($this, s, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor <= $this.limit_backward) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor - 1);
	if (ch > max || ch < min) {
		($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
		return true;
	}
	ch -= min;
	if ((s[ch >>> 3] & 0x1 << (ch & 0x7)) === 0) {
		($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
		return true;
	}
	return false;
}

BaseStemmer.out_grouping_b$LBaseStemmer$AIII = BaseStemmer$out_grouping_b$LBaseStemmer$AIII;

BaseStemmer.prototype.in_range$II = function (min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor >= this.limit) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor);
	if (ch > max || ch < min) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	return true;
};


function BaseStemmer$in_range$LBaseStemmer$II($this, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor >= $this.limit) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor);
	if (ch > max || ch < min) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	return true;
}

BaseStemmer.in_range$LBaseStemmer$II = BaseStemmer$in_range$LBaseStemmer$II;

BaseStemmer.prototype.in_range_b$II = function (min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor <= this.limit_backward) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor - 1);
	if (ch > max || ch < min) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	return true;
};


function BaseStemmer$in_range_b$LBaseStemmer$II($this, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor <= $this.limit_backward) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor - 1);
	if (ch > max || ch < min) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	return true;
}

BaseStemmer.in_range_b$LBaseStemmer$II = BaseStemmer$in_range_b$LBaseStemmer$II;

BaseStemmer.prototype.out_range$II = function (min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor >= this.limit) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor);
	if (! (ch > max || ch < min)) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	return true;
};


function BaseStemmer$out_range$LBaseStemmer$II($this, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor >= $this.limit) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor);
	if (! (ch > max || ch < min)) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	return true;
}

BaseStemmer.out_range$LBaseStemmer$II = BaseStemmer$out_range$LBaseStemmer$II;

BaseStemmer.prototype.out_range_b$II = function (min, max) {
	var ch;
	var $__jsx_postinc_t;
	if (this.cursor <= this.limit_backward) {
		return false;
	}
	ch = this.current.charCodeAt(this.cursor - 1);
	if (! (ch > max || ch < min)) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	return true;
};


function BaseStemmer$out_range_b$LBaseStemmer$II($this, min, max) {
	var ch;
	var $__jsx_postinc_t;
	if ($this.cursor <= $this.limit_backward) {
		return false;
	}
	ch = $this.current.charCodeAt($this.cursor - 1);
	if (! (ch > max || ch < min)) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	return true;
}

BaseStemmer.out_range_b$LBaseStemmer$II = BaseStemmer$out_range_b$LBaseStemmer$II;

BaseStemmer.prototype.eq_s$IS = function (s_size, s) {
	var cursor$0;
	if (((this.limit - this.cursor) | 0) < s_size) {
		return false;
	}
	if (this.current.slice(cursor$0 = this.cursor, ((cursor$0 + s_size) | 0)) !== s) {
		return false;
	}
	this.cursor = (this.cursor + s_size) | 0;
	return true;
};


function BaseStemmer$eq_s$LBaseStemmer$IS($this, s_size, s) {
	var cursor$0;
	if ((($this.limit - $this.cursor) | 0) < s_size) {
		return false;
	}
	if ($this.current.slice(cursor$0 = $this.cursor, ((cursor$0 + s_size) | 0)) !== s) {
		return false;
	}
	$this.cursor = ($this.cursor + s_size) | 0;
	return true;
}

BaseStemmer.eq_s$LBaseStemmer$IS = BaseStemmer$eq_s$LBaseStemmer$IS;

BaseStemmer.prototype.eq_s_b$IS = function (s_size, s) {
	var cursor$0;
	if (((this.cursor - this.limit_backward) | 0) < s_size) {
		return false;
	}
	if (this.current.slice((((cursor$0 = this.cursor) - s_size) | 0), cursor$0) !== s) {
		return false;
	}
	this.cursor = (this.cursor - s_size) | 0;
	return true;
};


function BaseStemmer$eq_s_b$LBaseStemmer$IS($this, s_size, s) {
	var cursor$0;
	if ((($this.cursor - $this.limit_backward) | 0) < s_size) {
		return false;
	}
	if ($this.current.slice((((cursor$0 = $this.cursor) - s_size) | 0), cursor$0) !== s) {
		return false;
	}
	$this.cursor = ($this.cursor - s_size) | 0;
	return true;
}

BaseStemmer.eq_s_b$LBaseStemmer$IS = BaseStemmer$eq_s_b$LBaseStemmer$IS;

BaseStemmer.prototype.eq_v$S = function (s) {
	return BaseStemmer$eq_s$LBaseStemmer$IS(this, s.length, s);
};


function BaseStemmer$eq_v$LBaseStemmer$S($this, s) {
	return BaseStemmer$eq_s$LBaseStemmer$IS($this, s.length, s);
}

BaseStemmer.eq_v$LBaseStemmer$S = BaseStemmer$eq_v$LBaseStemmer$S;

BaseStemmer.prototype.eq_v_b$S = function (s) {
	return BaseStemmer$eq_s_b$LBaseStemmer$IS(this, s.length, s);
};


function BaseStemmer$eq_v_b$LBaseStemmer$S($this, s) {
	return BaseStemmer$eq_s_b$LBaseStemmer$IS($this, s.length, s);
}

BaseStemmer.eq_v_b$LBaseStemmer$S = BaseStemmer$eq_v_b$LBaseStemmer$S;

BaseStemmer.prototype.find_among$ALAmong$I = function (v, v_size) {
	var i;
	var j;
	var c;
	var l;
	var common_i;
	var common_j;
	var first_key_inspected;
	var k;
	var diff;
	var common;
	var w;
	var i2;
	var res;
	i = 0;
	j = v_size;
	c = this.cursor;
	l = this.limit;
	common_i = 0;
	common_j = 0;
	first_key_inspected = false;
	while (true) {
		k = i + (j - i >>> 1);
		diff = 0;
		common = (common_i < common_j ? common_i : common_j);
		w = v[k];
		for (i2 = common; i2 < w.s_size; i2++) {
			if (c + common === l) {
				diff = -1;
				break;
			}
			diff = this.current.charCodeAt(c + common) - w.s.charCodeAt(i2);
			if (diff !== 0) {
				break;
			}
			common++;
		}
		if (diff < 0) {
			j = k;
			common_j = common;
		} else {
			i = k;
			common_i = common;
		}
		if (j - i <= 1) {
			if (i > 0) {
				break;
			}
			if (j === i) {
				break;
			}
			if (first_key_inspected) {
				break;
			}
			first_key_inspected = true;
		}
	}
	while (true) {
		w = v[i];
		if (common_i >= w.s_size) {
			this.cursor = (c + w.s_size | 0);
			if (w.method == null) {
				return w.result;
			}
			res = w.method(w.instance);
			this.cursor = (c + w.s_size | 0);
			if (res) {
				return w.result;
			}
		}
		i = w.substring_i;
		if (i < 0) {
			return 0;
		}
	}
	return -1;
};


function BaseStemmer$find_among$LBaseStemmer$ALAmong$I($this, v, v_size) {
	var i;
	var j;
	var c;
	var l;
	var common_i;
	var common_j;
	var first_key_inspected;
	var k;
	var diff;
	var common;
	var w;
	var i2;
	var res;
	i = 0;
	j = v_size;
	c = $this.cursor;
	l = $this.limit;
	common_i = 0;
	common_j = 0;
	first_key_inspected = false;
	while (true) {
		k = i + (j - i >>> 1);
		diff = 0;
		common = (common_i < common_j ? common_i : common_j);
		w = v[k];
		for (i2 = common; i2 < w.s_size; i2++) {
			if (c + common === l) {
				diff = -1;
				break;
			}
			diff = $this.current.charCodeAt(c + common) - w.s.charCodeAt(i2);
			if (diff !== 0) {
				break;
			}
			common++;
		}
		if (diff < 0) {
			j = k;
			common_j = common;
		} else {
			i = k;
			common_i = common;
		}
		if (j - i <= 1) {
			if (i > 0) {
				break;
			}
			if (j === i) {
				break;
			}
			if (first_key_inspected) {
				break;
			}
			first_key_inspected = true;
		}
	}
	while (true) {
		w = v[i];
		if (common_i >= w.s_size) {
			$this.cursor = (c + w.s_size | 0);
			if (w.method == null) {
				return w.result;
			}
			res = w.method(w.instance);
			$this.cursor = (c + w.s_size | 0);
			if (res) {
				return w.result;
			}
		}
		i = w.substring_i;
		if (i < 0) {
			return 0;
		}
	}
	return -1;
}

BaseStemmer.find_among$LBaseStemmer$ALAmong$I = BaseStemmer$find_among$LBaseStemmer$ALAmong$I;

BaseStemmer.prototype.find_among_b$ALAmong$I = function (v, v_size) {
	var i;
	var j;
	var c;
	var lb;
	var common_i;
	var common_j;
	var first_key_inspected;
	var k;
	var diff;
	var common;
	var w;
	var i2;
	var res;
	i = 0;
	j = v_size;
	c = this.cursor;
	lb = this.limit_backward;
	common_i = 0;
	common_j = 0;
	first_key_inspected = false;
	while (true) {
		k = i + (j - i >> 1);
		diff = 0;
		common = (common_i < common_j ? common_i : common_j);
		w = v[k];
		for (i2 = w.s_size - 1 - common; i2 >= 0; i2--) {
			if (c - common === lb) {
				diff = -1;
				break;
			}
			diff = this.current.charCodeAt(c - 1 - common) - w.s.charCodeAt(i2);
			if (diff !== 0) {
				break;
			}
			common++;
		}
		if (diff < 0) {
			j = k;
			common_j = common;
		} else {
			i = k;
			common_i = common;
		}
		if (j - i <= 1) {
			if (i > 0) {
				break;
			}
			if (j === i) {
				break;
			}
			if (first_key_inspected) {
				break;
			}
			first_key_inspected = true;
		}
	}
	while (true) {
		w = v[i];
		if (common_i >= w.s_size) {
			this.cursor = (c - w.s_size | 0);
			if (w.method == null) {
				return w.result;
			}
			res = w.method(this);
			this.cursor = (c - w.s_size | 0);
			if (res) {
				return w.result;
			}
		}
		i = w.substring_i;
		if (i < 0) {
			return 0;
		}
	}
	return -1;
};


function BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I($this, v, v_size) {
	var i;
	var j;
	var c;
	var lb;
	var common_i;
	var common_j;
	var first_key_inspected;
	var k;
	var diff;
	var common;
	var w;
	var i2;
	var res;
	i = 0;
	j = v_size;
	c = $this.cursor;
	lb = $this.limit_backward;
	common_i = 0;
	common_j = 0;
	first_key_inspected = false;
	while (true) {
		k = i + (j - i >> 1);
		diff = 0;
		common = (common_i < common_j ? common_i : common_j);
		w = v[k];
		for (i2 = w.s_size - 1 - common; i2 >= 0; i2--) {
			if (c - common === lb) {
				diff = -1;
				break;
			}
			diff = $this.current.charCodeAt(c - 1 - common) - w.s.charCodeAt(i2);
			if (diff !== 0) {
				break;
			}
			common++;
		}
		if (diff < 0) {
			j = k;
			common_j = common;
		} else {
			i = k;
			common_i = common;
		}
		if (j - i <= 1) {
			if (i > 0) {
				break;
			}
			if (j === i) {
				break;
			}
			if (first_key_inspected) {
				break;
			}
			first_key_inspected = true;
		}
	}
	while (true) {
		w = v[i];
		if (common_i >= w.s_size) {
			$this.cursor = (c - w.s_size | 0);
			if (w.method == null) {
				return w.result;
			}
			res = w.method($this);
			$this.cursor = (c - w.s_size | 0);
			if (res) {
				return w.result;
			}
		}
		i = w.substring_i;
		if (i < 0) {
			return 0;
		}
	}
	return -1;
}

BaseStemmer.find_among_b$LBaseStemmer$ALAmong$I = BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I;

BaseStemmer.prototype.replace_s$IIS = function (c_bra, c_ket, s) {
	var adjustment;
	adjustment = ((s.length - (((c_ket - c_bra) | 0))) | 0);
	this.current = this.current.slice(0, c_bra) + s + this.current.slice(c_ket);
	this.limit = (this.limit + adjustment) | 0;
	if (this.cursor >= c_ket) {
		this.cursor = (this.cursor + adjustment) | 0;
	} else if (this.cursor > c_bra) {
		this.cursor = c_bra;
	}
	return (adjustment | 0);
};


function BaseStemmer$replace_s$LBaseStemmer$IIS($this, c_bra, c_ket, s) {
	var adjustment;
	adjustment = ((s.length - (((c_ket - c_bra) | 0))) | 0);
	$this.current = $this.current.slice(0, c_bra) + s + $this.current.slice(c_ket);
	$this.limit = ($this.limit + adjustment) | 0;
	if ($this.cursor >= c_ket) {
		$this.cursor = ($this.cursor + adjustment) | 0;
	} else if ($this.cursor > c_bra) {
		$this.cursor = c_bra;
	}
	return (adjustment | 0);
}

BaseStemmer.replace_s$LBaseStemmer$IIS = BaseStemmer$replace_s$LBaseStemmer$IIS;

BaseStemmer.prototype.slice_check$ = function () {
	var bra$0;
	var ket$0;
	var limit$0;
	return ((bra$0 = this.bra) < 0 || bra$0 > (ket$0 = this.ket) || ket$0 > (limit$0 = this.limit) || limit$0 > this.current.length ? false : true);
};


function BaseStemmer$slice_check$LBaseStemmer$($this) {
	var bra$0;
	var ket$0;
	var limit$0;
	return ((bra$0 = $this.bra) < 0 || bra$0 > (ket$0 = $this.ket) || ket$0 > (limit$0 = $this.limit) || limit$0 > $this.current.length ? false : true);
}

BaseStemmer.slice_check$LBaseStemmer$ = BaseStemmer$slice_check$LBaseStemmer$;

BaseStemmer.prototype.slice_from$S = function (s) {
	var result;
	var bra$0;
	var ket$0;
	var limit$0;
	result = false;
	if ((bra$0 = this.bra) < 0 || bra$0 > (ket$0 = this.ket) || ket$0 > (limit$0 = this.limit) || limit$0 > this.current.length ? false : true) {
		BaseStemmer$replace_s$LBaseStemmer$IIS(this, this.bra, this.ket, s);
		result = true;
	}
	return result;
};


function BaseStemmer$slice_from$LBaseStemmer$S($this, s) {
	var result;
	var bra$0;
	var ket$0;
	var limit$0;
	result = false;
	if ((bra$0 = $this.bra) < 0 || bra$0 > (ket$0 = $this.ket) || ket$0 > (limit$0 = $this.limit) || limit$0 > $this.current.length ? false : true) {
		BaseStemmer$replace_s$LBaseStemmer$IIS($this, $this.bra, $this.ket, s);
		result = true;
	}
	return result;
}

BaseStemmer.slice_from$LBaseStemmer$S = BaseStemmer$slice_from$LBaseStemmer$S;

BaseStemmer.prototype.slice_del$ = function () {
	return BaseStemmer$slice_from$LBaseStemmer$S(this, "");
};


function BaseStemmer$slice_del$LBaseStemmer$($this) {
	return BaseStemmer$slice_from$LBaseStemmer$S($this, "");
}

BaseStemmer.slice_del$LBaseStemmer$ = BaseStemmer$slice_del$LBaseStemmer$;

BaseStemmer.prototype.insert$IIS = function (c_bra, c_ket, s) {
	var adjustment;
	adjustment = BaseStemmer$replace_s$LBaseStemmer$IIS(this, c_bra, c_ket, s);
	if (c_bra <= this.bra) {
		this.bra = (this.bra + adjustment) | 0;
	}
	if (c_bra <= this.ket) {
		this.ket = (this.ket + adjustment) | 0;
	}
};


function BaseStemmer$insert$LBaseStemmer$IIS($this, c_bra, c_ket, s) {
	var adjustment;
	adjustment = BaseStemmer$replace_s$LBaseStemmer$IIS($this, c_bra, c_ket, s);
	if (c_bra <= $this.bra) {
		$this.bra = ($this.bra + adjustment) | 0;
	}
	if (c_bra <= $this.ket) {
		$this.ket = ($this.ket + adjustment) | 0;
	}
}

BaseStemmer.insert$LBaseStemmer$IIS = BaseStemmer$insert$LBaseStemmer$IIS;

BaseStemmer.prototype.slice_to$S = function (s) {
	var result;
	var bra$0;
	var ket$0;
	var limit$0;
	result = '';
	if ((bra$0 = this.bra) < 0 || bra$0 > (ket$0 = this.ket) || ket$0 > (limit$0 = this.limit) || limit$0 > this.current.length ? false : true) {
		result = this.current.slice(this.bra, this.ket);
	}
	return result;
};


function BaseStemmer$slice_to$LBaseStemmer$S($this, s) {
	var result;
	var bra$0;
	var ket$0;
	var limit$0;
	result = '';
	if ((bra$0 = $this.bra) < 0 || bra$0 > (ket$0 = $this.ket) || ket$0 > (limit$0 = $this.limit) || limit$0 > $this.current.length ? false : true) {
		result = $this.current.slice($this.bra, $this.ket);
	}
	return result;
}

BaseStemmer.slice_to$LBaseStemmer$S = BaseStemmer$slice_to$LBaseStemmer$S;

BaseStemmer.prototype.assign_to$S = function (s) {
	return this.current.slice(0, this.limit);
};


function BaseStemmer$assign_to$LBaseStemmer$S($this, s) {
	return $this.current.slice(0, $this.limit);
}

BaseStemmer.assign_to$LBaseStemmer$S = BaseStemmer$assign_to$LBaseStemmer$S;

BaseStemmer.prototype.stem$ = function () {
	return false;
};


BaseStemmer.prototype.stemWord$S = function (word) {
	var result;
	var current$0;
	var cursor$0;
	var limit$0;
	result = this.cache['.' + word];
	if (result == null) {
		current$0 = this.current = word;
		cursor$0 = this.cursor = 0;
		limit$0 = this.limit = current$0.length;
		this.limit_backward = 0;
		this.bra = cursor$0;
		this.ket = limit$0;
		this.stem$();
		result = this.current;
		this.cache['.' + word] = result;
	}
	return result;
};

BaseStemmer.prototype.stemWord = BaseStemmer.prototype.stemWord$S;

BaseStemmer.prototype.stemWords$AS = function (words) {
	var results;
	var i;
	var word;
	var result;
	var current$0;
	var cursor$0;
	var limit$0;
	results = [  ];
	for (i = 0; i < words.length; i++) {
		word = words[i];
		result = this.cache['.' + word];
		if (result == null) {
			current$0 = this.current = word;
			cursor$0 = this.cursor = 0;
			limit$0 = this.limit = current$0.length;
			this.limit_backward = 0;
			this.bra = cursor$0;
			this.ket = limit$0;
			this.stem$();
			result = this.current;
			this.cache['.' + word] = result;
		}
		results.push(result);
	}
	return results;
};

BaseStemmer.prototype.stemWords = BaseStemmer.prototype.stemWords$AS;

function DanishStemmer() {
	BaseStemmer.call(this);
	this.I_x = 0;
	this.I_p1 = 0;
	this.S_ch = "";
}

$__jsx_extend([DanishStemmer], BaseStemmer);
DanishStemmer.prototype.copy_from$LDanishStemmer$ = function (other) {
	this.I_x = other.I_x;
	this.I_p1 = other.I_p1;
	this.S_ch = other.S_ch;
	BaseStemmer$copy_from$LBaseStemmer$LBaseStemmer$(this, other);
};

DanishStemmer.prototype.copy_from = DanishStemmer.prototype.copy_from$LDanishStemmer$;

DanishStemmer.prototype.r_mark_regions$ = function () {
	var v_1;
	var v_2;
	var c;
	var lab1;
	var lab3;
	var lab4;
	var cursor$0;
	var limit$0;
	var cursor$1;
	var cursor$2;
	var $__jsx_postinc_t;
	this.I_p1 = limit$0 = this.limit;
	v_1 = cursor$0 = this.cursor;
	c = (cursor$0 + 3 | 0);
	if (0 > c || c > limit$0) {
		return false;
	}
	cursor$2 = this.cursor = c;
	this.I_x = cursor$2;
	this.cursor = v_1;
golab0:
	while (true) {
		v_2 = this.cursor;
		lab1 = true;
	while (lab1 === true) {
        lab1 = false;
        if (! BaseStemmer$in_grouping$LBaseStemmer$AIII(this, DanishStemmer.g_v, 97, 248)) {
            break;
        }
        this.cursor = v_2;
        break golab0;
    }
		cursor$1 = this.cursor = v_2;
		if (cursor$1 >= this.limit) {
			return false;
		}
		($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	}
golab2:
	while (true) {
		lab3 = true;
	while (lab3 === true) {
        lab3 = false;
        if (! BaseStemmer$out_grouping$LBaseStemmer$AIII(this, DanishStemmer.g_v, 97, 248)) {
            break;
        }
        break golab2;
    }
		if (this.cursor >= this.limit) {
			return false;
		}
		($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	}
	this.I_p1 = this.cursor;
	lab4 = true;
while (lab4 === true) {
    lab4 = false;
    if (! (this.I_p1 < this.I_x)) {
        break;
    }
    this.I_p1 = this.I_x;
}
	return true;
};

DanishStemmer.prototype.r_mark_regions = DanishStemmer.prototype.r_mark_regions$;

function DanishStemmer$r_mark_regions$LDanishStemmer$($this) {
	var v_1;
	var v_2;
	var c;
	var lab1;
	var lab3;
	var lab4;
	var cursor$0;
	var limit$0;
	var cursor$1;
	var cursor$2;
	var $__jsx_postinc_t;
	$this.I_p1 = limit$0 = $this.limit;
	v_1 = cursor$0 = $this.cursor;
	c = (cursor$0 + 3 | 0);
	if (0 > c || c > limit$0) {
		return false;
	}
	cursor$2 = $this.cursor = c;
	$this.I_x = cursor$2;
	$this.cursor = v_1;
golab0:
	while (true) {
		v_2 = $this.cursor;
		lab1 = true;
	while (lab1 === true) {
        lab1 = false;
        if (! BaseStemmer$in_grouping$LBaseStemmer$AIII($this, DanishStemmer.g_v, 97, 248)) {
            break;
        }
        $this.cursor = v_2;
        break golab0;
    }
		cursor$1 = $this.cursor = v_2;
		if (cursor$1 >= $this.limit) {
			return false;
		}
		($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	}
golab2:
	while (true) {
		lab3 = true;
	while (lab3 === true) {
        lab3 = false;
        if (! BaseStemmer$out_grouping$LBaseStemmer$AIII($this, DanishStemmer.g_v, 97, 248)) {
            break;
        }
        break golab2;
    }
		if ($this.cursor >= $this.limit) {
			return false;
		}
		($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t + 1) | 0, $__jsx_postinc_t);
	}
	$this.I_p1 = $this.cursor;
	lab4 = true;
while (lab4 === true) {
    lab4 = false;
    if (! ($this.I_p1 < $this.I_x)) {
        break;
    }
    $this.I_p1 = $this.I_x;
}
	return true;
}

DanishStemmer.r_mark_regions$LDanishStemmer$ = DanishStemmer$r_mark_regions$LDanishStemmer$;

DanishStemmer.prototype.r_main_suffix$ = function () {
	var among_var;
	var v_1;
	var v_2;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	v_1 = ((this.limit - (cursor$0 = this.cursor)) | 0);
	if (cursor$0 < this.I_p1) {
		return false;
	}
	cursor$1 = this.cursor = this.I_p1;
	v_2 = this.limit_backward;
	this.limit_backward = cursor$1;
	cursor$2 = this.cursor = ((this.limit - v_1) | 0);
	this.ket = cursor$2;
	among_var = BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I(this, DanishStemmer.a_0, 32);
	if (among_var === 0) {
		this.limit_backward = v_2;
		return false;
	}
	this.bra = this.cursor;
	this.limit_backward = v_2;
	switch (among_var) {
	case 0:
		return false;
	case 1:
		if (! BaseStemmer$slice_from$LBaseStemmer$S(this, "")) {
			return false;
		}
		break;
	case 2:
		if (! BaseStemmer$in_grouping_b$LBaseStemmer$AIII(this, DanishStemmer.g_s_ending, 97, 229)) {
			return false;
		}
		if (! BaseStemmer$slice_from$LBaseStemmer$S(this, "")) {
			return false;
		}
		break;
	}
	return true;
};

DanishStemmer.prototype.r_main_suffix = DanishStemmer.prototype.r_main_suffix$;

function DanishStemmer$r_main_suffix$LDanishStemmer$($this) {
	var among_var;
	var v_1;
	var v_2;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	v_1 = (($this.limit - (cursor$0 = $this.cursor)) | 0);
	if (cursor$0 < $this.I_p1) {
		return false;
	}
	cursor$1 = $this.cursor = $this.I_p1;
	v_2 = $this.limit_backward;
	$this.limit_backward = cursor$1;
	cursor$2 = $this.cursor = (($this.limit - v_1) | 0);
	$this.ket = cursor$2;
	among_var = BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I($this, DanishStemmer.a_0, 32);
	if (among_var === 0) {
		$this.limit_backward = v_2;
		return false;
	}
	$this.bra = $this.cursor;
	$this.limit_backward = v_2;
	switch (among_var) {
	case 0:
		return false;
	case 1:
		if (! BaseStemmer$slice_from$LBaseStemmer$S($this, "")) {
			return false;
		}
		break;
	case 2:
		if (! BaseStemmer$in_grouping_b$LBaseStemmer$AIII($this, DanishStemmer.g_s_ending, 97, 229)) {
			return false;
		}
		if (! BaseStemmer$slice_from$LBaseStemmer$S($this, "")) {
			return false;
		}
		break;
	}
	return true;
}

DanishStemmer.r_main_suffix$LDanishStemmer$ = DanishStemmer$r_main_suffix$LDanishStemmer$;

DanishStemmer.prototype.r_consonant_pair$ = function () {
	var v_1;
	var v_2;
	var v_3;
	var limit$0;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	var cursor$3;
	var limit_backward$0;
	var $__jsx_postinc_t;
	v_1 = (((limit$0 = this.limit) - (cursor$0 = this.cursor)) | 0);
	v_2 = ((limit$0 - cursor$0) | 0);
	if (cursor$0 < this.I_p1) {
		return false;
	}
	cursor$1 = this.cursor = this.I_p1;
	v_3 = this.limit_backward;
	this.limit_backward = cursor$1;
	cursor$2 = this.cursor = ((this.limit - v_2) | 0);
	this.ket = cursor$2;
	if (BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I(this, DanishStemmer.a_1, 4) === 0) {
		this.limit_backward = v_3;
		return false;
	}
	this.bra = this.cursor;
	limit_backward$0 = this.limit_backward = v_3;
	cursor$3 = this.cursor = ((this.limit - v_1) | 0);
	if (cursor$3 <= limit_backward$0) {
		return false;
	}
	($__jsx_postinc_t = this.cursor, this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	this.bra = this.cursor;
	return (! BaseStemmer$slice_from$LBaseStemmer$S(this, "") ? false : true);
};

DanishStemmer.prototype.r_consonant_pair = DanishStemmer.prototype.r_consonant_pair$;

function DanishStemmer$r_consonant_pair$LDanishStemmer$($this) {
	var v_1;
	var v_2;
	var v_3;
	var limit$0;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	var cursor$3;
	var limit_backward$0;
	var $__jsx_postinc_t;
	v_1 = (((limit$0 = $this.limit) - (cursor$0 = $this.cursor)) | 0);
	v_2 = ((limit$0 - cursor$0) | 0);
	if (cursor$0 < $this.I_p1) {
		return false;
	}
	cursor$1 = $this.cursor = $this.I_p1;
	v_3 = $this.limit_backward;
	$this.limit_backward = cursor$1;
	cursor$2 = $this.cursor = (($this.limit - v_2) | 0);
	$this.ket = cursor$2;
	if (BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I($this, DanishStemmer.a_1, 4) === 0) {
		$this.limit_backward = v_3;
		return false;
	}
	$this.bra = $this.cursor;
	limit_backward$0 = $this.limit_backward = v_3;
	cursor$3 = $this.cursor = (($this.limit - v_1) | 0);
	if (cursor$3 <= limit_backward$0) {
		return false;
	}
	($__jsx_postinc_t = $this.cursor, $this.cursor = ($__jsx_postinc_t - 1) | 0, $__jsx_postinc_t);
	$this.bra = $this.cursor;
	return (! BaseStemmer$slice_from$LBaseStemmer$S($this, "") ? false : true);
}

DanishStemmer.r_consonant_pair$LDanishStemmer$ = DanishStemmer$r_consonant_pair$LDanishStemmer$;

DanishStemmer.prototype.r_other_suffix$ = function () {
	var among_var;
	var v_1;
	var v_2;
	var v_3;
	var v_4;
	var lab0;
	var lab1;
	var limit$0;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	v_1 = ((this.limit - this.cursor) | 0);
	lab0 = true;
while (lab0 === true) {
    lab0 = false;
    this.ket = this.cursor;
    if (! BaseStemmer$eq_s_b$LBaseStemmer$IS(this, 2, "st")) {
        break;
    }
    this.bra = this.cursor;
    if (! BaseStemmer$eq_s_b$LBaseStemmer$IS(this, 2, "ig")) {
        break;
    }
    if (! BaseStemmer$slice_from$LBaseStemmer$S(this, "")) {
        return false;
    }
}
	cursor$0 = this.cursor = (((limit$0 = this.limit) - v_1) | 0);
	v_2 = ((limit$0 - cursor$0) | 0);
	if (cursor$0 < this.I_p1) {
		return false;
	}
	cursor$1 = this.cursor = this.I_p1;
	v_3 = this.limit_backward;
	this.limit_backward = cursor$1;
	cursor$2 = this.cursor = ((this.limit - v_2) | 0);
	this.ket = cursor$2;
	among_var = BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I(this, DanishStemmer.a_2, 5);
	if (among_var === 0) {
		this.limit_backward = v_3;
		return false;
	}
	this.bra = this.cursor;
	this.limit_backward = v_3;
	switch (among_var) {
	case 0:
		return false;
	case 1:
		if (! BaseStemmer$slice_from$LBaseStemmer$S(this, "")) {
			return false;
		}
		v_4 = ((this.limit - this.cursor) | 0);
		lab1 = true;
	while (lab1 === true) {
        lab1 = false;
        if (! DanishStemmer$r_consonant_pair$LDanishStemmer$(this)) {
            break;
        }
    }
		this.cursor = ((this.limit - v_4) | 0);
		break;
	case 2:
		if (! BaseStemmer$slice_from$LBaseStemmer$S(this, "l\u00F8s")) {
			return false;
		}
		break;
	}
	return true;
};

DanishStemmer.prototype.r_other_suffix = DanishStemmer.prototype.r_other_suffix$;

function DanishStemmer$r_other_suffix$LDanishStemmer$($this) {
	var among_var;
	var v_1;
	var v_2;
	var v_3;
	var v_4;
	var lab0;
	var lab1;
	var limit$0;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	v_1 = (($this.limit - $this.cursor) | 0);
	lab0 = true;
while (lab0 === true) {
    lab0 = false;
    $this.ket = $this.cursor;
    if (! BaseStemmer$eq_s_b$LBaseStemmer$IS($this, 2, "st")) {
        break;
    }
    $this.bra = $this.cursor;
    if (! BaseStemmer$eq_s_b$LBaseStemmer$IS($this, 2, "ig")) {
        break;
    }
    if (! BaseStemmer$slice_from$LBaseStemmer$S($this, "")) {
        return false;
    }
}
	cursor$0 = $this.cursor = (((limit$0 = $this.limit) - v_1) | 0);
	v_2 = ((limit$0 - cursor$0) | 0);
	if (cursor$0 < $this.I_p1) {
		return false;
	}
	cursor$1 = $this.cursor = $this.I_p1;
	v_3 = $this.limit_backward;
	$this.limit_backward = cursor$1;
	cursor$2 = $this.cursor = (($this.limit - v_2) | 0);
	$this.ket = cursor$2;
	among_var = BaseStemmer$find_among_b$LBaseStemmer$ALAmong$I($this, DanishStemmer.a_2, 5);
	if (among_var === 0) {
		$this.limit_backward = v_3;
		return false;
	}
	$this.bra = $this.cursor;
	$this.limit_backward = v_3;
	switch (among_var) {
	case 0:
		return false;
	case 1:
		if (! BaseStemmer$slice_from$LBaseStemmer$S($this, "")) {
			return false;
		}
		v_4 = (($this.limit - $this.cursor) | 0);
		lab1 = true;
	while (lab1 === true) {
        lab1 = false;
        if (! DanishStemmer$r_consonant_pair$LDanishStemmer$($this)) {
            break;
        }
    }
		$this.cursor = (($this.limit - v_4) | 0);
		break;
	case 2:
		if (! BaseStemmer$slice_from$LBaseStemmer$S($this, "l\u00F8s")) {
			return false;
		}
		break;
	}
	return true;
}

DanishStemmer.r_other_suffix$LDanishStemmer$ = DanishStemmer$r_other_suffix$LDanishStemmer$;

DanishStemmer.prototype.r_undouble$ = function () {
	var v_1;
	var v_2;
	var s$0;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	var S_ch$0;
	v_1 = ((this.limit - (cursor$0 = this.cursor)) | 0);
	if (cursor$0 < this.I_p1) {
		return false;
	}
	cursor$1 = this.cursor = this.I_p1;
	v_2 = this.limit_backward;
	this.limit_backward = cursor$1;
	cursor$2 = this.cursor = ((this.limit - v_1) | 0);
	this.ket = cursor$2;
	if (! BaseStemmer$out_grouping_b$LBaseStemmer$AIII(this, DanishStemmer.g_v, 97, 248)) {
		this.limit_backward = v_2;
		return false;
	}
	this.bra = this.cursor;
	S_ch$0 = this.S_ch = BaseStemmer$slice_to$LBaseStemmer$S(this, this.S_ch);
	if (S_ch$0 === '') {
		return false;
	}
	this.limit_backward = v_2;
	return (! (s$0 = this.S_ch, BaseStemmer$eq_s_b$LBaseStemmer$IS(this, s$0.length, s$0)) ? false : ! BaseStemmer$slice_from$LBaseStemmer$S(this, "") ? false : true);
};

DanishStemmer.prototype.r_undouble = DanishStemmer.prototype.r_undouble$;

function DanishStemmer$r_undouble$LDanishStemmer$($this) {
	var v_1;
	var v_2;
	var s$0;
	var cursor$0;
	var cursor$1;
	var cursor$2;
	var S_ch$0;
	v_1 = (($this.limit - (cursor$0 = $this.cursor)) | 0);
	if (cursor$0 < $this.I_p1) {
		return false;
	}
	cursor$1 = $this.cursor = $this.I_p1;
	v_2 = $this.limit_backward;
	$this.limit_backward = cursor$1;
	cursor$2 = $this.cursor = (($this.limit - v_1) | 0);
	$this.ket = cursor$2;
	if (! BaseStemmer$out_grouping_b$LBaseStemmer$AIII($this, DanishStemmer.g_v, 97, 248)) {
		$this.limit_backward = v_2;
		return false;
	}
	$this.bra = $this.cursor;
	S_ch$0 = $this.S_ch = BaseStemmer$slice_to$LBaseStemmer$S($this, $this.S_ch);
	if (S_ch$0 === '') {
		return false;
	}
	$this.limit_backward = v_2;
	return (! (s$0 = $this.S_ch, BaseStemmer$eq_s_b$LBaseStemmer$IS($this, s$0.length, s$0)) ? false : ! BaseStemmer$slice_from$LBaseStemmer$S($this, "") ? false : true);
}

DanishStemmer.r_undouble$LDanishStemmer$ = DanishStemmer$r_undouble$LDanishStemmer$;

DanishStemmer.prototype.stem$ = function () {
	var v_1;
	var v_2;
	var v_3;
	var v_4;
	var lab0;
	var lab1;
	var lab2;
	var lab3;
	var lab4;
	var cursor$0;
	var limit$0;
	var cursor$1;
	var limit$1;
	var cursor$2;
	var limit$2;
	var cursor$3;
	v_1 = this.cursor;
	lab0 = true;
while (lab0 === true) {
    lab0 = false;
    if (! DanishStemmer$r_mark_regions$LDanishStemmer$(this)) {
        break;
    }
}
	cursor$0 = this.cursor = v_1;
	this.limit_backward = cursor$0;
	cursor$1 = this.cursor = limit$0 = this.limit;
	v_2 = ((limit$0 - cursor$1) | 0);
	lab1 = true;
while (lab1 === true) {
    lab1 = false;
    if (! DanishStemmer$r_main_suffix$LDanishStemmer$(this)) {
        break;
    }
}
	cursor$2 = this.cursor = (((limit$1 = this.limit) - v_2) | 0);
	v_3 = ((limit$1 - cursor$2) | 0);
	lab2 = true;
while (lab2 === true) {
    lab2 = false;
    if (! DanishStemmer$r_consonant_pair$LDanishStemmer$(this)) {
        break;
    }
}
	cursor$3 = this.cursor = (((limit$2 = this.limit) - v_3) | 0);
	v_4 = ((limit$2 - cursor$3) | 0);
	lab3 = true;
while (lab3 === true) {
    lab3 = false;
    if (! DanishStemmer$r_other_suffix$LDanishStemmer$(this)) {
        break;
    }
}
	this.cursor = ((this.limit - v_4) | 0);
	lab4 = true;
while (lab4 === true) {
    lab4 = false;
    if (! DanishStemmer$r_undouble$LDanishStemmer$(this)) {
        break;
    }
}
	this.cursor = this.limit_backward;
	return true;
};

DanishStemmer.prototype.stem = DanishStemmer.prototype.stem$;

DanishStemmer.prototype.equals$X = function (o) {
	return o instanceof DanishStemmer;
};

DanishStemmer.prototype.equals = DanishStemmer.prototype.equals$X;

function DanishStemmer$equals$LDanishStemmer$X($this, o) {
	return o instanceof DanishStemmer;
}

DanishStemmer.equals$LDanishStemmer$X = DanishStemmer$equals$LDanishStemmer$X;

DanishStemmer.prototype.hashCode$ = function () {
	var classname;
	var hash;
	var i;
	var char;
	classname = "DanishStemmer";
	hash = 0;
	for (i = 0; i < classname.length; i++) {
		char = classname.charCodeAt(i);
		hash = (hash << 5) - hash + char;
		hash = hash & hash;
	}
	return (hash | 0);
};

DanishStemmer.prototype.hashCode = DanishStemmer.prototype.hashCode$;

function DanishStemmer$hashCode$LDanishStemmer$($this) {
	var classname;
	var hash;
	var i;
	var char;
	classname = "DanishStemmer";
	hash = 0;
	for (i = 0; i < classname.length; i++) {
		char = classname.charCodeAt(i);
		hash = (hash << 5) - hash + char;
		hash = hash & hash;
	}
	return (hash | 0);
}

DanishStemmer.hashCode$LDanishStemmer$ = DanishStemmer$hashCode$LDanishStemmer$;

DanishStemmer.serialVersionUID = 1;
$__jsx_lazy_init(DanishStemmer, "methodObject", function () {
	return new DanishStemmer();
});
$__jsx_lazy_init(DanishStemmer, "a_0", function () {
	return [ new Among("hed", -1, 1), new Among("ethed", 0, 1), new Among("ered", -1, 1), new Among("e", -1, 1), new Among("erede", 3, 1), new Among("ende", 3, 1), new Among("erende", 5, 1), new Among("ene", 3, 1), new Among("erne", 3, 1), new Among("ere", 3, 1), new Among("en", -1, 1), new Among("heden", 10, 1), new Among("eren", 10, 1), new Among("er", -1, 1), new Among("heder", 13, 1), new Among("erer", 13, 1), new Among("s", -1, 2), new Among("heds", 16, 1), new Among("es", 16, 1), new Among("endes", 18, 1), new Among("erendes", 19, 1), new Among("enes", 18, 1), new Among("ernes", 18, 1), new Among("eres", 18, 1), new Among("ens", 16, 1), new Among("hedens", 24, 1), new Among("erens", 24, 1), new Among("ers", 16, 1), new Among("ets", 16, 1), new Among("erets", 28, 1), new Among("et", -1, 1), new Among("eret", 30, 1) ];
});
$__jsx_lazy_init(DanishStemmer, "a_1", function () {
	return [ new Among("gd", -1, -1), new Among("dt", -1, -1), new Among("gt", -1, -1), new Among("kt", -1, -1) ];
});
$__jsx_lazy_init(DanishStemmer, "a_2", function () {
	return [ new Among("ig", -1, 1), new Among("lig", 0, 1), new Among("elig", 1, 1), new Among("els", -1, 1), new Among("l\u00F8st", -1, 2) ];
});
DanishStemmer.g_v = [ 17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 128 ];
DanishStemmer.g_s_ending = [ 239, 254, 42, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16 ];

var $__jsx_classMap = {
	"src/among.jsx": {
		Among: Among,
		Among$SII: Among,
		Among$SIIF$LBaseStemmer$B$LBaseStemmer$: Among$0
	},
	"src/stemmer.jsx": {
		Stemmer: Stemmer,
		Stemmer$: Stemmer
	},
	"src/base-stemmer.jsx": {
		BaseStemmer: BaseStemmer,
		BaseStemmer$: BaseStemmer
	},
	"src/danish-stemmer.jsx": {
		DanishStemmer: DanishStemmer,
		DanishStemmer$: DanishStemmer
	}
};


})(JSX);

var Among = JSX.require("src/among.jsx").Among;
var Among$SII = JSX.require("src/among.jsx").Among$SII;
var Stemmer = JSX.require("src/stemmer.jsx").Stemmer;
var BaseStemmer = JSX.require("src/base-stemmer.jsx").BaseStemmer;
var DanishStemmer = JSX.require("src/danish-stemmer.jsx").DanishStemmer;
